from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm


# Create your views here.
class CustomLogin(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('todolist:todo')
        form = LoginForm
        context = {
            "form": form,
        }
        return render(request, 'user/login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('todolist:todo')
        messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')
        return redirect('user:login')
    