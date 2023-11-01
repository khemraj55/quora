from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import User, Question, Answer
from .forms import UserForm, QuestionForm, AnswerForm
from django.shortcuts import get_object_or_404

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password).first()
        if user:
          
            request.session['user_id'] = user.id
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout(request):

    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('login')

def home(request):
    questions = Question.objects.all()
    return render(request, 'home.html', {'questions': questions})



def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        try:
            if form.is_valid():
                question = form.save(commit=False)
                user_id = request.session.get('user_id')
                user = get_object_or_404(User, pk=user_id)
                question.user = user
                question.save()
                return redirect('home')
        except User.DoesNotExist as e:
            return HttpResponseNotFound("User matching query does not exist")
        except Exception as e:
            return HttpResponseNotFound("An error occurred: {}".format(e), status=500)
    else:
        form = QuestionForm()
    return render(request, 'ask_question.html', {'form': form})

def answer_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        try:
            if form.is_valid():
                answer = form.save(commit=False)
                user_id = request.session.get('user_id')
                user = get_object_or_404(User, pk=user_id)
                answer.user = user
                answer.question = question
                answer.save()
                return redirect('home')
        except User.DoesNotExist as e:
            return HttpResponseNotFound("User matching query does not exist")
        except Exception as e:
            return HttpResponseNotFound("An error occurred: {}".format(e), status=500)
    else:
        form = AnswerForm()
    return render(request, 'answer_question.html', {'form': form, 'question': question})

def like_answer(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    user_id = request.session.get('user_id')
    user = get_object_or_404(User, pk=user_id)
    answer.likes.add(user)
    return redirect('home')

