from django.urls import  path
from . import views
app_name='student'

urlpatterns=[
    path('index',views.home),     
    path('ProfileManagement',views.ProfileManagement,name='Profile'),
    path('AttendanceReport',views.Attendance, name='Att'),
    path('HomeWork',views.HomeWork , name='HomeWork'),
    path('ProgressCard',views.ProgressCard, name='ProgressCard'),
    path('Assignments',views.Assignment, name='Assign' ),
    path('Notice',views.Notice, name='Notice'),
    path('Fees',views.Fees, name='Fees'),

]