from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path ('', views.index, name='list'),
    path ('<int:question_id>/', views.detail, name='detail'),
    path ('<int:question_id>/answer/create/', views.answer_create, name='answer_create'),
    path ('question/create/', views.question_create, name='question_create'),
]