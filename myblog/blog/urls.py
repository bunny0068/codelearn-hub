from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    path("", views.blog, name='blogpage'),
    path("post/<int:pk>/", views.post_detail, name='post_detail'),
    path("create/", views.create_post, name="create_post"),
    path("update/<int:pk>/",views.update_post,name='update_post'),
    path("delete/<int:pk>/",views.delete_post,name='delete_post'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='blog:blogpage'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('comment/delete/<int:pk>/', views.delete_comment, name='delete_comment'),
    path('comment/update/<int:pk>/', views.update_comment, name='update_comment'),
    path('profile/', views.profile, name='profile'),
]
