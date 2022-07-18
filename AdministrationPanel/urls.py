from django.urls import path
from . import views
app_name = 'Administration'

urlpatterns = [
    path('index', views.home, name='index'),
    path('ProfileManagement', views.ProfileManagement, name='Profile'),
    path('AttendanceReport', views.Attendance, name='Att'),
    path('Assignments', views.Assignment, name='Assign'),
    path('Notice', views.Notice, name='Notice'),
    path('Fees', views.FeesReport, name='Fees'),
    path('Exams', views.Exams, name='Exams'),
    path('Student', views.Student, name='Student'),
    path('Teacher', views.Teacher, name='Teacher'),
    path('ChangePassword', views.ChangePassword, name='ChangePassword'),
    path('AdminLogin', views.AdminLogin, name='AdminLogin'),
    path('signup',views.signup, name='signup'),
    path('Admindashboard', views.Admindashboard, name='Admindashboard'),



]
