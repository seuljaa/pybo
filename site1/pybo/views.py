from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Question,Answer
from .forms import Question_form

# Create your views here.

def index(request):
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'question_list':page_obj}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'pybo/question_detail.html', {'question':question})

def answer_create(request, question_id):
    question = Question.objects.get(id=question_id)
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    return redirect('pybo:detail', question_id=question.id)

def question_create(request):
    if request.method == 'POST':
        form = Question_form(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:list')
    else:
        form = Question_form()
        context = {'form':form}
    return render(request, 'pybo/question_create.html', context)