from urllib import request
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from djangoProject.krupskoi.models import Kalitka, Vorota, Premission

from rest_framework import  status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from djangoProject.krupskoi.serializers import VhodSerializer, VhodSerializer1
from django.contrib.auth.models import User

from collections import namedtuple

nt = namedtuple("object", ["model", "serializers"])
pattern = {
    "kalitka" : nt(Kalitka, VhodSerializer),
    "vorota" : nt(Vorota, VhodSerializer1),

}

def change_status(api_name):
    try:
        obj = Kalitka.objects.get(entry_name=api_name)
        obj.entry_code = False
        obj.save()

    except:
        pass

    try:
        obj = Vorota.objects.get(entry_name=api_name)
        obj.entry_code = False
        obj.save()

    except:
        pass




@api_view(["GET", "POST"])
def ListView(request, api_name):
    object = pattern.get(api_name, None)
    if object == None:
        return Response(
            data="Invalid URL",
            status=status.HTTP_404_NOT_FOUND,
        )
    if request.method == "GET":
        object_list = object.model.objects.all()
        serializers = object.serializers(object_list, many=True)
        src = serializers.data
        change_status(api_name)
        return Response(src)

    if request.method == "POST":
        data = request.data
        serializers = object.serializers(data=data)

        if not serializers.is_valid():
            return Response(
                data=serializers.error,
                status=status.HTTP_404_NOT_FOUND
            )
        serializers.save()
        return Response(
            data=serializers.error,
            status=status.HTTP_201_CREATED
        )


def index(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                var = int(request.POST["kalitka"])
                obj = Kalitka.objects.get(entry_name='kalitka')
                obj.entry_code = True
                obj.save()
            except:
                pass

            try:
                var = int(request.POST["vorota"])
                obj = Vorota.objects.get(entry_name='vorota')
                obj.entry_code = True
                obj.save()

            except:
                pass

            return HttpResponseRedirect('/')
    else:
        return redirect('signin')



    context={
        "vorota": Vorota.objects.get(entry_name='vorota'),
        "kalitka": Kalitka.objects.get(entry_name='kalitka'),
        "prem": Premission.objects.get(user=request.user)
    }
    return render(request, 'index.html', context)

def signin(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return render(request, 'signin.html')

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            # Return an 'invalid login' error message.
            return redirect('signin')

def signup(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return render(request, 'signup.html')

    if request.method == 'POST':
        try:
            user = User.objects.create_user(username=request.POST["phone"],first_name=request.POST["username"], last_name=request.POST["kvartira"], password=request.POST["password"])
            user.save()
            prem = Premission.objects.create(user=user)
            prem.save()
            login(request, user)
            return redirect('index')
        except:
            return redirect('signup')
    else:
        return redirect('signup')

def logoutuser(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('signin')
    else:
        return redirect('signin')
