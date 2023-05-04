from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path(
        '<slug:post>/',
        views.post_detail,
        name='post_detail'
    ),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:post_id>/share/',  views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment')
]