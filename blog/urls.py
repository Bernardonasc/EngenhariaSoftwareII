from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    # Rotas de autenticação:
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html', next_page='post_list'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='post_list'), name='logout'),
    path('register/', views.register, name='register'),
    path('autor/<str:username>/', views.post_list_by_author, name='post_list_by_author'),
    path('categoria/<slug:slug>/', views.post_list_by_category, name='post_list_by_category'),
]
