from django.urls import  path
from . import views
app_name='Administration'

urlpatterns=[
    path('index',views.home, name='index'),     
    path('ProfileManagement',views.ProfileManagement, name='Profile'),
    path('AttendanceReport',views.Attendance, name='Att'),     
    path('Assignments',views.Assignment, name='Assign' ),
    path('Notice',views.Notice, name='Notice'),
    path('Fees',views.FeesReport, name='Fees'),
    path('Exams',views.Exams, name='Exams'),
    path('Students',views.Students, name='Students'),
    path('Teachers',views.Teachers, name='Teachers'),
    path('ChangePassword',views.ChangePassword, name='ChangePassword'),

    
]
