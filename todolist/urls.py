from django.urls import path
from . import views

app_name = 'todolist'

urlpatterns = [
    # 인덱스페이지
    path('', views.Index.as_view(), name='index'),
    # 리스트 페이지
    path('list/', views.TodoList.as_view(), name='todo'),
    path('list/<int:category_id>', views.TodoList.as_view(), name='todo-detail'),
    # 카테고리
    path('list/category/write', views.CategoryWrite.as_view(), name='category-write'),
    path('list/<int:category_id>/delete', views.CategoryDelete.as_view(), name='category-delete'),
    path('list/<int:category_id>/update', views.CategoryUpdate.as_view(), name='category-update'),
    # 할일
    path('list/<int:category_id>/todo/write', views.TodoWrite.as_view(), name='todo-write'),
    path('list/todo/<int:todo_id>/delete', views.TodoDelete.as_view(), name='todo-delete'),
    path('list/todo/<int:todo_id>/update', views.TodoUpdate.as_view(), name='todo-update'),
    path('list/todo/<int:todo_id>/toggle', views.TodoClearToggle.as_view(), name='todo-toggle'),
]