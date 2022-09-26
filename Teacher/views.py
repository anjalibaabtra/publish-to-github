from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from administrationpanel.models import AdminUser

# Create your views here.

def home(request):
    return render(request, 'Administration/index.html')

def Profile(request):
    return render(request, 'Teacher/Profile.html')
    

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

# def TeacherLogin(request):
#     return render(request, 'Teacher/TeacherLogin.html')

# def signup(request):
#     return render(request, 'Teacher/signup.html')

def TeacherDashboard(request):
    return render(request, 'Teacher/TeacherDashboard.html')

# def signup(request):
#     if request.method=='POST':
#         uname=request.POST["uname"]
#         email=request.POST["email"]
#         password=request.POST["password"]
#         if TeacherUser.objects.filter(Username=uname).exists():
#             messages.info(request,'Username already used')
#             # return redirect('signup'
#             return render(request,'Teacher/signup.html')
#         elif TeacherUser.objects.filter(Email=email).exists():
#             messages.info(request,'Email already used')
#             # return redirect('signup')
#             return render(request,'Teacher/signup.html')
#         else:
#             user_data=TeacherUser(Username=uname, Email=email, Password=password)
#             user_data.save()
#             # return redirect('AdminLogin')
#             return render(request,'Teacher/TeacherLogin.html')
#     else:
#         return render(request,'Teacher/signup.html')


def signup(request):
    if request.method=='POST':
        uname=request.POST["uname"]
        email=request.POST["email"]
        password=request.POST["password"]
        if AdminUser.objects.filter(username=uname).exists():
            messages.info(request,'Username already used')
            # return redirect('signup')

            return render(request,'Teacher/signup.html')

        elif AdminUser.objects.filter(email=email).exists():
            messages.info(request,'Email already used')
            # return redirect('signup')
            return render(request,'Teacher/signup.html')
        else:
            user_data=AdminUser.objects.create_user(username=uname, email=email, password=password, is_teacher=True)
            user_data.save()
            # return redirect('AdminLogin')
            return render(request,'Teacher/TeacherLogin.html')
    else:
        return render(request,'Teacher/signup.html')

def TeacherLogin(request):
    if request.method=='POST':
        uname=request.POST['uname']
        password=request.POST['password']            
        user = authenticate(request, username=uname, password=password)
        if user is not None and user.is_teacher:            
            login(request, user)
            # return redirect("dashboard")
            return render(request, 'Teacher/TeacherDashboard.html')
        else:
            messages.info(request,'Invalid Username or Password')
            # return redirect('TeacherLogin')
            return render(request, 'Teacher/TeacherLogin.html')
    else:
        return render(request, 'Teacher/TeacherLogin.html')

def StudentsRegister(request):
    return render(request, 'Teacher/StudentsRegister.html')

def StudentsMarks(request):
    return render(request, 'Teacher/StudentsMarks.html')

def TimeTable(request):
    return render(request, 'Teacher/TimeTable.html')


def Teacherlogout(request):
    logout(request)
    # return render(request, '../Administration/index.html')
    return redirect('../Administration/index')






