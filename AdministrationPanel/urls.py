from django.urls import path
from . import views
app_name = 'Administration'

urlpatterns = [
    path('index', views.home, name='index'),
    path('AddAttendance', views.AddAttendance, name='AddAttendance'),
    path('Attendance', views.Attendance, name='Attendance'),
    path('Assignments', views.Assignment, name='Assign'),
    path('Notice', views.Notice, name='Notice'),
    path('Fees', views.Fees, name='Fees'),
    path('Exams', views.Exams, name='Exams'),
    path('Student', views.Student, name='Student'),
    path('Teacher', views.Teacher, name='Teacher'),
    path('ChangePassword', views.ChangePassword, name='ChangePassword'),
    path('AdminLogin', views.AdminLogin, name='AdminLogin'),
    path('signup', views.signup, name='signup'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('Teachers', views.Teachers, name='Teachers'),
    path('Students', views.Students, name='Students'),




]
