from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'Teacher/index.html')

def ProfileManagement(request):
    return render(request,'Teacher/Profile.html')
    

def Attendance(request):
    return render(request, 'Teacher/Attd.html')

def HomeWork(request):
    return render(request,'Teacher/Hwork.html')

def ProgressCard(request):
    return render(request,'Teacher/PrgsCard.html')

def Assignment(request):
    return render(request,'Teacher/Assign.html')

def Notice(request):
    return render(request,'Teacher/Notice.html')










