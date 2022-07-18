from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'Administration/index.html')

def ProfileManagement(request):
    return render(request,'Administration/ProfileMgnt.html')    


def Attendance(request):
    return render(request, 'Administration/Attendance.html')

def Student(request):
    return render(request,'Student/StudentLogin.html')

def Teacher(request):
    return render(request,'Teacher/TeacherLogin.html')


def Assignment(request):
    return render(request,'Administration/Assignment.html')

def FeesReport(request):
    return render(request,'Administration/Fees.html')

def Exams(request):
    return render(request,'Administration/Exams.html')

def ChangePassword(request):
    return render(request,'Administration/ChangePassword.html')

def Notice(request):
    return render(request,'Administration/Notice.html')

def AdminLogin(request):
    return render(request,'Administration/AdminLogin.html')

def signup(request):
    return render(request, 'Administration/signup.html')
    
def Admindashboard(request):
    return render(request, 'Administration/Admindashboard.html')






