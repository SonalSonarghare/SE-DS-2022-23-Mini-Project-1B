"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),

    
    path('admin_login',views.admin_login,name='admin_login'),
    path('register',views.register,name='register'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('admin_profile',views.admin_profile,name='admin_profile'),
    path('admin_add_emp',views.admin_add_emp,name='admin_add_emp'),
    path('attendance_record',views.attendance_record,name='attendance_record'),
    path('admin_add_project',views.admin_add_project,name='admin_add_project'),
    path('show_emp',views.show_emp,name='show_emp'),

    path('emp_login',views.emp_login,name='emp_login'),
    path('emp_dashboard',views.emp_dashboard,name='emp_dashboard'),
    path('emp_profile',views.emp_profile,name='emp_profile'),
    path('mark_attendance',views.mark_attendance,name='mark_attendance'),
    path('emp_attendance_record',views.emp_attendance_record,name='emp_attendance_record'),
    path('emp_show_emp',views.emp_show_emp,name='emp_show_emp'),
    
    path('Assigned_task',views.Assigned_task,name='Assigned_task'),
    path('Assigned_task_admin',views.Assigned_task_admin,name = 'Assigned_task_admin')    


]
