from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'Student/index.html')

def ProfileManagement(request):
    return render(request,'Student/Profile.html')    


def Attendance(request):
    return render(request, 'Student/Attd.html')


def HomeWork(request):
    return render(request,'Student/Hwork.html')

def ProgressCard(request):
    return render(request,'Student/PrgsCard.html')

def Assignment(request):
    return render(request,'Student/Assign.html')

def Fees(request):
    return render(request,'Student/Fees.html')

def Notice(request):
    return render(request,'Student/Notice.html')



