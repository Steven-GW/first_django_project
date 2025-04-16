from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name="list"),
    path('<slug:slug>', views.post_page, name="page"),
    path('newpost/', views.newpost, name='newpost'),
    path('edit_post/<int:id>/', views.edit_post, name='edit_post'),
    path('logoutt/', views.logoutt, name='logoutt')
]