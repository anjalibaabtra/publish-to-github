from unicodedata import name
from django.urls import URLPattern, path
from . import views

app_name='teacher'

urlpatterns=[
    path('index',views.home, name='ind'),     
    path('ProfileManagement',views.ProfileManagement,name='Profile'),
    path('AttendanceReport',views.Attendance, name='Att'),
    path('HomeWork',views.HomeWork , name='HomeWork'),
    path('ProgressCard',views.ProgressCard, name='ProgressCard'),
    path('Assignments',views.Assignment, name='Assign' ),
    path('Notice',views.Notice, name='Notice'),
]
