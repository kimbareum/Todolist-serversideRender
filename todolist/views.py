from django.shortcuts import render, redirect
from django.views import View
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category, Post


# Create your views here.
class Index(View):

    def get(self, request):
        return render(request, 'todolist/index.html')


class TodoList(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user
        categories = Category.objects.filter(user=user)[::-1]
        try:
            posts = Post.objects.filter(category=categories[0].pk)[::-1]
        except:
            posts = {}

        context = {
            'categories': categories,
            'posts': posts,
        }

        return render(request, 'todolist/todo.html', context)