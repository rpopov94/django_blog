from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path(
        '<slug:post>/',
        views.post_detail,
        name='post_detail'
    ),
    path('', views.PostListView.as_view(), name='post_list')
]