from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Question
from .forms import QuestionForm, AnswerForm

def index(request):
    """
    목록출력
    """
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date')
    pagenator = Paginator(question_list, 10)

    page_obj = pagenator.get_page(page)
    context = {'list' : page_obj}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    상세내용출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    """
    답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid() :
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    """
    질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else :
        form = QuestionForm()
        return render(request, 'pybo/question_form.html', {'form':form})