from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from pybo.forms import CommentForm
from pybo.models import Question,Comment, Answer

# 질문_댓글_작성
@login_required(login_url='common:login')
def comment_create_question(request, question_id):
    """
    pybo 질문댓글등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.question = question
            comment.save()
            return redirect('pybo:detail', question_id=question.id)
    else :
        form = CommentForm()
        context = {'form':form}
    return render(request, 'pybo/comment_form.html', context)

# 질문_댓글_수정
@login_required(login_url='common:login')
def comment_modify_question(request, comment_id):
    """
    pybo_질문댓글수정
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author :
        messages.error('수정권한이 없습니다!')
        return redirect('pybo:detail', question_id=comment.question.id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('pybo:detail', question_id=comment.question.id)
    else:
        form = CommentForm(instance=comment)
        context = {'form':form}
    return render(request, 'pybo/comment_form.html', context)

# 질문_댓글_삭제
@login_required(login_url='common:login')
def comment_delete_question(request, comment_id):
    """
    pybo_질문삭제
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author :
        messages.error('삭제권한이 없습니다!')
        return redirect('pybo:detail', question_id=comment.question.id)
    else :
        comment.delete()
    return redirect('pybo:detail', question_id=comment.question.id)

# 답변_댓글_작성
@login_required(login_url='common:login')
def comment_create_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()
            return redirect('pybo:detail', question_id=Answer.question.id)
    else :
        form = CommentForm()
        context = {'form':form}
    return render(request, 'pybo/comment_form.html', context)

# 답변_댓글_수정
@login_required(login_url='common:login')
def comment_modify_answer(request, comment_id):
    return

# 답변_댓글_삭제
@login_required(login_url='common:login')
def comment_delete_answer(request, comment_id):
    return