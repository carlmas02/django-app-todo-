from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Note

def home(request):
    data = Note.objects.filter(user=request.user)
    context = {
        'data':data
    }
    return render(request,"home.html",context)

def signup(request):
    

    return render(request,'signup.html')

def loginpage(request):
    if request.method == "POST":
        user = request.POST['username']
        passw = request.POST['password']

        user = authenticate(request,username=user,password = passw)

        if user is not None:
            login(request,user)
            return redirect('home')
        else :
            print("Invalid Login")              



    return render(request,'login.html')

def note(request,id):

    data = Note.objects.get(id =id)

    context = {

        "data" :data 

    }
    return render(request,'note.html',context)

def add(request):
    if request.method == "POST":
        title = request.POST['title']
        task = request.POST['task']
        print(title,task)

        note_object = Note.objects.create(user=request.user,title=title,task=task)
        note_object.save()

        return redirect('home')

    return render(request,'add.html')

def delete(request,id):

    note_object = Note.objects.get(id=id)
    note_object.delete()

    return redirect('home')
    pass

def logout_user(request):
    logout(request)

    return redirect('login')