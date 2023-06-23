from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'user'

urlpatterns = [
    path("login/", views.CustomLogin.as_view(), name='login'),
    path("logout/", LogoutView.as_view(next_page="todolist:index"), name='logout'),
    # path('', views.Index.as_view(), name='index'),
    # path('', views.index), # FBV
    # path('', views.Index.as_view(), name='list'), # CBV
    # path('write/', views.write, name='write'),
    # 제네릭뷰
    # path('', views.List.as_view(), name='list'),
    # path('write/', views.Write.as_view(), name='write'),
    # path('detail/<int:post_id>/', views.DetailView.as_view(), name='detail'),
    # path('detail/<int:pk>/edit', views.Update.as_view(), name='edit'),
    # path('detail/<int:pk>/delete', views.Delete.as_view(), name='delete'),
    # # 코멘트
    # path('detail/<int:post_id>/comment/write', views.CommentWrite.as_view(), name='cm-write'),
    # path('detail/comment/<int:comment_id>/delete', views.CommentDelete.as_view(), name='cm-delete'),
    # # 태그
    # path('detail/<int:post_id>/tag/write', views.HashTagWrite.as_view(), name='tag-write'),
    # path('detail/tag/<int:hashTag_id>/delete', views.HashTagDelete.as_view(), name='tag-delete'),
]