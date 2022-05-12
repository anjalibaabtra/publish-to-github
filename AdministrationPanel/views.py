from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'Administration/index.html')

def ProfileManagement(request):
    return render(request,'Administration/ProfileMgnt.html')    


def Attendance(request):
    return render(request, 'Administration/Attendance.html')

def Students(request):
    return render(request,'Administration/Students.html')

def Teachers(request):
    return render(request,'Administration/Teachers.html')


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




