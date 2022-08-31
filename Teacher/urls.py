from django.urls import  path
from . import views
app_name='Teacher'

urlpatterns=[
    path('index',views.home, name='index'),     
    path('ProfileManagement',views.ProfileManagement,name='ProfileManagement'),
    path('AttendanceReport',views.Attendance, name='AttendanceReport'),
    path('HomeWork',views.HomeWork , name='HomeWork'),
    path('ProgressCard',views.ProgressCard, name='ProgressCard'),
    path('Assignments',views.Assignment, name='Assignment' ),
    path('Notice',views.Notice, name='Notice'),
    path('TeacherLogin',views.TeacherLogin, name='TeacherLogin'),
    path('signup',views.signup, name='signup'),
    path('TeacherDashboard',views.TeacherDashboard, name='TeacherDashboard'),



]
