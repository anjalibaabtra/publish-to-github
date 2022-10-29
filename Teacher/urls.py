from django.urls import  path
from . import views
app_name='Teacher'

urlpatterns=[
    path('index',views.home, name='index'),     
    path('Profile',views.Profile,name='Profile'),
    path('ChangePassword',views.ChangePassword,name='ChangePassword'),
    path('Attendance',views.Attendance, name='Attendance'),
    path('AttendanceReport',views.AttendanceReport, name='AttendanceReport'),
    path('ViewAttendance',views.ViewAttendance, name='ViewAttendance'),
    path('HomeWork',views.HomeWork , name='HomeWork'),
    path('ProgressCard',views.ProgressCard, name='ProgressCard'),
    path('Assignments',views.Assignment, name='Assignment' ),
    path('Notice',views.Notice, name='Notice'),
    path('TeacherLogin',views.TeacherLogin, name='TeacherLogin'),
    path('signup',views.signup, name='signup'),
    path('TeacherDashboard',views.TeacherDashboard, name='TeacherDashboard'),
    path('StudentsRegister',views.StudentsRegister, name='StudentsRegister'),
    path('StudentsMarks',views.StudentsMarks, name='StudentsMarks'),
    path('TimeTable',views.TimeTable, name='TimeTable'),
    path('AddAttendance',views.AddAttendance, name='AddAttendance'),
    path('ViewAttendance',views.ViewAttendance, name='ViewAttendance'),
    path('Fees',views.Fees, name='Fees'),
    path('FeeDues',views.FeeDues, name='FeeDues'),
    path('logout', views.Teacherlogout, name='logout'),

]
