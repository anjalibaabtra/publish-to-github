from django.urls import path
from . import views
app_name = 'Administration'

urlpatterns = [
    path('index', views.home, name='index'),
    path('AddAttendance', views.AddAttendance, name='AddAttendance'),
    path('Attendance', views.Attendance, name='Attendance'),
    path('AttendanceReport', views.AttendanceReport, name='AttendanceReport'),
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
    path('ViewAllStudents', views.ViewAllStudents, name='ViewAllStudents'),
    path('ViewAllTeachers', views.ViewAllTeachers, name='ViewAllTeachers'),
    path('AddTeachers', views.AddTeachers, name='AddTeachers'),
    path('ApproveTeachers', views.ApproveTeachers, name='ApproveTeachers'),
    path('Teacherssalary', views.Teacherssalary, name='Teacherssalary'),
    path('AddStudents', views.AddStudents, name='AddStudents'),
    path('ApproveStudents', views.ApproveStudents, name='ApproveStudents'),
    path('Approve<int:StudentId>', views.ApproveStd, name='Approve'),
    # path('update/<int:Employeesid>', views.updateEmployees, name='update'),
    path('FeeofStudents', views.FeeofStudents, name='FeeofStudents'),
    path('FeeDues', views.FeeDues, name='FeeDues'),
    path('ViewAttendance', views.ViewAttendance, name='ViewAttendance'),    
    path('logout', views.Adminlogout, name='logout'),



]
