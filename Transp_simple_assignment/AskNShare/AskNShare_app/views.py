from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from AskNShare_app.models import Answer, Add_question


# Create your views here.

def login_function(request):
        return render(request, 'login.html')

def login_read_fun(request):
    user1 = authenticate(username=request.POST['utext'], password=request.POST['pwtext'])
    if user1 is not None:
        request.session['username'] = request.POST['utext']
        return render(request, 'home.html', {'data': '','uname':request.session['username']})
    else:
        return render(request, 'login.html', {'data': 'Username or password does not exist'})


def register_fun(request):
    return render(request, 'register.html', {'Error_Message': ''})

def reg_redata(request):

    if User.objects.filter(Q(username=request.POST['User']) | Q(email=request.POST['email'])).exists():
        return render(request, 'register.html', {'Error_Message': 'Username and Email is already exist!'})
    else:
        u1 = User.objects.create_superuser(username=request.POST['User'], email=request.POST['email'],
                                           password=request.POST['pw'])
        u1.save()
        return redirect('log')


def home_function(request):
    return render(request,'home.html',{'uname':''})


def add_question(request):
    return render(request,'add_ques.html')


def answer_fun(request):
    q1=Add_question.objects.all()
    return render(request,'answer.html',{'data':q1})


def logout_fun(request):
    response = HttpResponse()
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return render(request, 'logout.html')


def add_question_read(request):
    q1=Add_question()
    q1.question=request.POST['questext']
    q1.save()
    return redirect('ans')


def read_answer(request,id):
    # if request.method == 'POST':
    a1=Answer()
    a1.answer=request.POST['annstext']
    a1.like=0
    a1.ques_id=id
    a1.user_name=request.session['username']
    a1.save()
    return redirect('ans')



def view_ans_fun(request,id):
    a1=Answer.objects.filter(ques_id__exact=id)
    return render(request,'view_ans.html',{'data':a1})


def create_ans_fun(request,id):
    q1=Add_question.objects.get(id=id)
    return render(request,'create_ans.html',{'id':id,'ques':q1})


def like_an_fun(request,id):
    a1=Answer.objects.get(id=id)
    return render(request,'like_ans.html',{'like_data':a1})


def like_read_fun(request,id):
    a1 = Answer.objects.get(id=id)
    a1.like = a1.like + 1
    a1.save()
    a2=Answer.objects.get(id=id)
    id=a2.ques_id
    return redirect('va', id)
