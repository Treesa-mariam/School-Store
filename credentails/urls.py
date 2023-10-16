from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('register/', TemplateView.as_view(template_name='register'), name='register'),
    path('login/', views.login, name='login'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('logout/', views.logout, name='logout'),
]
