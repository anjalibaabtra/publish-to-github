from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from administrationpanel.models import AdminUser

# Create your views here.


def home(request):
    return render(request, 'Administration/index.html')


def Profile(request):
    return render(request, 'Student/Profile.html')


def AttendanceReport(request):
    return render(request, 'Student/AttendanceReport.html')


def HomeWork(request):
    return render(request, 'Student/HomeWork.html')


def ProgressCard(request):
    return render(request, 'Student/ProgressCard.html')


def Assignment(request):
    return render(request, 'Student/Assignment.html')


def Fees(request):
    return render(request, 'Student/Fees.html')


def Notice(request):
    return render(request, 'Student/Notice.html')


def StudentDashboard(request):
    return render(request, 'Student/StudentDashboard.html')


def signup(request):
    if request.method=='POST':
        uname=request.POST["uname"]
        email=request.POST["email"]
        password=request.POST["password"]
        if AdminUser.objects.filter(Username=uname).exists():
            messages.info(request,'Username already used')
            # return redirect('signup')

            return render(request,'Student/signup.html')

        elif AdminUser.objects.filter(Email=email).exists():
            messages.info(request,'Email already used')
            # return redirect('signup')
            return render(request,'Student/signup.html')
        else:
            user_data=AdminUser.objects.create_user(username=uname, email=email, password=password, is_student=True)
            user_data.save()
            # return redirect('AdminLogin')
            return render(request,'Student/StudentLogin.html')
    else:
        return render(request,'Student/signup.html')


def StudentLogin(request):
    if request.method=='POST':
        uname=request.POST['uname']
        password=request.POST['password']    
        is_student='true'    
        # obj = AdminUser.objects.first()
        user = authenticate(request, username=uname, password=password)
        # getuser = AdminUser.objects.get(id=user.)

        # print(check)
        if user is not None and user.is_student:
        # if user.is_student == True:
            print(user,uname,password)
            login(request, user)
            # return redirect("dashboard")
            return render(request, 'Student/StudentDashboard.html')
        else:
            print(user,uname,password)
            messages.info(request,'Invalid Username or Password')
            # return redirect('AdminLogin')
            return render(request, 'Student/StudentLogin.html')
    else:
        return render(request, 'Student/StudentLogin.html')
        

def Studentlogout(request):
    logout(request)
    # return render(request, 'Administration/index.html')
    return redirect('../Administration/index')
