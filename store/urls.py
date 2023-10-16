from django.urls import path
from . import views
app_name='store'

urlpatterns = [
    path('',views.home,name='home'),
    path('department/<int:department_id>/', views.department_wikipedia, name='department_wikipedia'),


]