from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'Teacher/index.html')

def ProfileManagement(request):
    return render(request, 'Teacher/ProfileManagement.html')
    

def Attendance(request):
    return render(request, 'Teacher/Attendance.html')

def HomeWork(request):
    return render(request, 'Teacher/HomeWork.html')

def ProgressCard(request):
    return render(request, 'Teacher/ProgresssCard.html')

def Assignment(request):
    return render(request, 'Teacher/Assignment.html')

def Notice(request):
    return render(request, 'Teacher/Notice.html')

def TeacherLogin(request):
    return render(request, 'Teacher/TeacherLogin.html')

def signup(request):
    return render(request, 'Teacher/signup.html')











