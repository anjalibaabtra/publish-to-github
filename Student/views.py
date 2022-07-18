from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'Student/index.html')

def ProfileManagement(request):
    return render(request, 'Student/ProfileManagement.html')    


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

def StudentLogin(request):
    return render(request, 'Student/StudentLogin.html')

def signup(request):
    return render(request, 'Student/signup.html')





