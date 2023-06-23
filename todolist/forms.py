from django import forms
from .models import Category, Todo


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name']


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['title', 'content']