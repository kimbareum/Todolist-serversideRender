from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from .models import Category, Todo
from .forms import CategoryForm, TodoForm


# Create your views here.
### 인덱스 페이지
class Index(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('todolist:todo')
        return render(request, 'todolist/index.html')


### 리스트 페이지
class TodoList(LoginRequiredMixin, View):

    def get(self, request, category_id=None):
        user = request.user
        categories = Category.objects.filter(user=user)[::-1]
        if categories:
            if category_id is None:
                category_id = categories[0].pk
            category_user = Category.objects.get(pk=category_id).user
            if category_user != user:
                return redirect('todolist:todo')
            todos = Todo.objects.filter(category=category_id)
        else:
            todos = {}

        context = {
            'categories': categories,
            'todos': todos,
            'category_id': category_id,
        }

        return render(request, 'todolist/todo.html', context)


### 카테고리 CRUD
class CategoryWrite(View):

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            category = Category.objects.create(name=name, user=user)
            return redirect('todolist:todo-detail', category_id=category.pk)


class CategoryDelete(View):

    def post(self, request, category_id):
        category = Category.objects.get(pk=category_id)
        category.delete()
        return redirect('todolist:todo')


class CategoryUpdate(View):

    def post(self, request, category_id):
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = Category.objects.get(pk=category_id)
            name = form.cleaned_data['name']
            category.name = name
            category.save()
            # return JsonResponse({'category_update': True})
            return redirect('todolist:todo-detail', category_id=category_id)


### 할일 CRUD
class TodoWrite(View):

    def post(self, request, category_id):
        form = TodoForm(request.POST)
        if form.is_valid():
            category = Category.objects.get(pk=category_id)
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            todo = Todo.objects.create(title=title, content=content, category=category)
            return redirect('todolist:todo-detail', category_id=category_id)


class TodoDelete(View):

    def post(self, request, todo_id):
        todo = Todo.objects.get(pk=todo_id)
        category_id = todo.category.id
        todo.delete()
        return redirect('todolist:todo-detail', category_id=category_id)


class TodoClearToggle(View):

    def post(self, request, todo_id):
        todo = Todo.objects.get(pk=todo_id)
        todo.is_clear = not todo.is_clear
        todo.save()
        category_id = todo.category.id
        return JsonResponse({'is_clear': todo.is_clear})
        # return redirect('todolist:todo-detail', category_id=category_id)


class TodoUpdate(View):

    def post(self, request, todo_id):
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = Todo.objects.get(pk=todo_id)
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            # category_id = todo.category.id
            todo.title = title
            todo.content = content
            todo.save()
            return JsonResponse({'todo_update': True})
            return redirect('todolist:todo-detail', category_id=category_id)
