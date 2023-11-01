from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('ask_question/', views.ask_question, name='ask_question'),
    path('answer_question/<int:question_id>/', views.answer_question, name='answer_question'),
    path('like_answer/<int:answer_id>/', views.like_answer, name='like_answer'),
    path('logout/', views.logout, name='logout'),
]