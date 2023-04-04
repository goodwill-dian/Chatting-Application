from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from django.contrib.auth import login, logout, authenticate
from .forms import LoginUserForm

import json


class ChatBox(viewsets.ModelViewSet):
    def chat_page(self, request):
        if not request.user.is_authenticated:
            return redirect('log_in')

        # context = {'username':request.user.first_name}
        # context_json = json.loads(context)
        # print(context['username'])

        return render(request, 'index_frontend.html')
        # return render(request, 'chat/index.html', context)
        

def get_data(request):
    # data = {
    #     'firstname': request.user.first_name,
    #     'lastname': request.user.last_name,
    # }
    data = {
        'username': request.user.username,
        'firstname': request.user.first_name,
        'lastname': request.user.last_name,
    }
    # print(data)
    return JsonResponse(json.dumps(data), safe=False)


class LogIn(viewsets.ModelViewSet):
    def log_in(self, request):
        username = request.data['username']
        password = request.data['password']
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('chat_page')
        
        form = LoginUserForm()
        return render(request, 'chat/login.html',{'form_login': form})
        
    def log_in_form(self, request):
        form = LoginUserForm()
        return render(request, 'chat/login.html',{'form_login': form})
            
class LogOut(viewsets.ModelViewSet):
    def log_out(self, request):
        logout(request)
        return redirect('log_in')
        
