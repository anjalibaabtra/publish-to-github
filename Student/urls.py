from django.urls import  path
from . import views
app_name='Student'

urlpatterns=[
    path('index',views.home, name='index'),     
    path('Profile',views.Profile, name='Profile'),
    path('AttendanceReport',views.AttendanceReport, name='AttendanceReport'),
    path('HomeWork',views.HomeWork , name='HomeWork'),
    path('ProgressCard',views.ProgressCard, name='ProgressCard'),
    path('Assignments',views.Assignment, name='Assignment' ),
    path('Notice',views.Notice, name='Notice'),
    path('Fees',views.Fees, name='Fees'),
    path('StudentLogin',views.StudentLogin, name='StudentLogin'),
    path('signup',views.signup, name='signup'),
    path('StudentDashboard',views.StudentDashboard, name='StudentDashboard'),
    path('logout', views.Studentlogout, name='logout'),
    
]
