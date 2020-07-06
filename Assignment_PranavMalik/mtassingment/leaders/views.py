from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.forms import User
from django.db import IntegrityError
from django.contrib.auth import login ,logout, authenticate
from .models import user_score,levels,tests,extendeduser
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'leaders/home.html')


def signupuser(request):
    if request.method=='GET': 
      return render(request,'leaders/signupuser.html',{'form':UserCreationForm()})
    
    else :
        if request.POST['password1']==request.POST['password2']:
            try:
              user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
              email=request.POST['email']
              age=request.POST['age']
              exuser=extendeduser(email=email,age=age,user=user)
              user.save()
              exuser.save()
              login(request,user)
              return redirect('tests')
            #Same Username Server Side Validation
            except IntegrityError:
                return render(request,'leaders/signupuser.html',{'form':UserCreationForm(),'error':'That username has already been taken Please choose a new username'})


        else:
            print('hello')
            return render(request,'leaders/signupuser.html',{'form':UserCreationForm(),'error':'Passwords did not match'})

def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method=='GET': 
      return render(request,'leaders/loginuser.html',{'form':AuthenticationForm()})
    else:
       user= authenticate(request,username=request.POST['username'],password=request.POST['password'])
       if user is None:
           return render(request,'leaders/loginuser.html',{'form':AuthenticationForm(),'error':'Username and Password donot match!'})
       else :
          login(request,user)
          return redirect('tests')

    
def tests(request):
     return render(request,'leaders/tests.html')

@login_required(login_url='/login/')
def showdata(request):
    data=user_score.objects.all().order_by('score').reverse()
    return render(request,'leaders/showdata.html',{'data':data})

@login_required(login_url='/login/')
def showdata2(request):
    data=user_score.objects.all().order_by('score').reverse()
    return render(request,'leaders/showdata2.html',{'data':data})






    
