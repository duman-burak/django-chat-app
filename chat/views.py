from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required

def index(request):
    users = User.objects.all().exclude(username=request.user)
    return render(request, "chat/index.html" ,{
        'users':users,
    })

@login_required(login_url='Login')
def room(request, room_name):   
    users = User.objects.all().exclude(username=request.user)
    room = Room.objects.get(id=room_name)
    messages = Message.objects.filter(room=room)
    sessiz_kisiler = Mute.objects.filter(muter=request.user)
    if request.method == 'POST':
        if request.POST.get("button")=="sessiz":
            user_id = request.POST.get("user_id")
            user = User.objects.get(id=user_id)
            sessiz_kisi = Mute.objects.create(muter=request.user,muted_user=user)
            sessiz_kisi.save()
            return redirect("/chat/"+ room_name + "/")
    return render(request, "chat/room2.html", {
        "room_name": room_name,
        'users' : users,
        'room' : room,
        'messages' : messages,
        'sessiz_kisiler' : sessiz_kisiler,
        })


@login_required(login_url='Login')
def start_chat(request,username):
    second_user = User.objects.get(username=username)
    try:
        room = Room.objects.get(first_user=request.user,second_user=second_user)
    except Room.DoesNotExist:
        try:
            room = Room.objects.get(second_user=request.user,first_user=second_user)
        except:
            Room.objects.create(first_user=request.user,second_user=second_user)
    return redirect("room",room.id)

@login_required(login_url='Login')
def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return redirect("Login")
    
    return render(request, "chat/login.html")

