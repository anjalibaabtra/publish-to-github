
import email
from django.shortcuts import render, redirect
from django.contrib import messages
from administrationpanel.models import AdminUser, StudentFee
from django.contrib.auth import authenticate, login, logout
from django.db.models import Subquery, OuterRef

# Create your views here.


def home(request):

    return render(request, 'Administration/index.html')


def AddAttendance(request):

    return render(request, 'Administration/AddAttendance.html')


def Attendance(request):

    return render(request, 'Administration/Attendance.html')


def AttendanceReport(request):
    return render(request, 'Administration/AttendanceReport.html')


def Student(request):

    return render(request, 'Student/StudentLogin.html')


def Teacher(request):
    return render(request, 'Teacher/TeacherLogin.html')


def Assignment(request):
    return render(request, 'Administration/Assignment.html')


def Fees(request):
    return render(request, 'Administration/Fees.html')


# def Fees(request):
#     return render(request, 'Administration/Fees.html')




# Employee.objects.annotate(
#     company_name=Subquery(
#         Company.objects.filter(location=OuterRef('location')).values('name')
#     )).values_list('name', 'company_name')

# field_name = 'name'
# obj = MyModel.objects.first()
# field_value = getattr(obj, field_name)

# field_object = MyModel._meta.get_field(field_name)



def FeeDues(request):
    allstudents = AdminUser.objects.filter(is_student=True)
    email_id='email'
    # email_id= AdminUser._meta.get_field(email)
    # print(email_id)
    obj = AdminUser.objects.first()
    # student=AdminUser.objects.get(email=mail_id)
    # student_email=Subquery(StudentFee.objects.filter(Email=OuterRef()))
    student_email =getattr(obj,email_id)
    print(student_email)
    allfees = StudentFee.objects.filter(Email=student_email)
    return render(request, 'Administration/FeeDues.html',{'students': allstudents,'fees':allfees})


def Exams(request):
    return render(request, 'Administration/Exams.html')


def ChangePassword(request):
    if request.method == "POST":
        Email = request.POST["email"]
        password = request.POST["pswd"]
        RptPassword = request.POST["rptpswd"]
        user = AdminUser.objects.get(email=Email) 
        if AdminUser.objects.filter(email=Email).exists() and user.is_admin:            
            if password == RptPassword:                  
                u = AdminUser.objects.get(username=user.username)
                # print(user.password)
                u.set_password(password)
                u.save()
                messages.info(request, 'Password has been changed')
                return render(request, 'Administration/AdminLogin.html')
            else:
                messages.info(request, 'Password does not match')
        else:
            messages.info(request, 'Email Does not Exist')
    return render(request, 'Administration/ChangePassword.html')


def Notice(request):
    return render(request, 'Administration/Notice.html')


# def AdminLogin(request):
#     return render(request, 'Administration/AdminLogin.html')


def dashboard(request):
    return render(request, 'Administration/dashboard.html')


def Students(request):

    return render(request, 'Administration/Students.html')


def Teachers(request):
    return render(request, 'Administration/Teachers.html')


def ViewAllStudents(request):
    allstudents = AdminUser.objects.filter(is_student=True)
    return render(request, 'Administration/ViewAllStudents.html', {'students': allstudents})


def ViewAllTeachers(request):
    allteachers = AdminUser.objects.filter(is_teacher=True)
    return render(request, 'Administration/ViewAllTeachers.html', {'teachers': allteachers})


def AddTeachers(request):

    if request.method == "POST":

        Name = request.POST["name"]
        Fname = request.POST["fname"]
        Lname = request.POST["lname"]
        Dob = request.POST["dob"]
        Gender = request.POST["gender"]
        AdmissionNum = request.POST["admnum"]
        Std = request.POST["std"]
        Division = request.POST["division"]
        Religion = request.POST["religion"]
        Bld = request.POST["bld"]
        Contact = request.POST["contact"]
        Subject = request.POST["subject"]
        Joindate = request.POST["joindate"]
        WorkExperience = request.POST["workexp"]
        Salary = request.POST["salary"]

        user = AdminUser.objects.get(username=Name)
        AdminUser.objects.filter(id=user.id).update(
            Name=Name, Firstname=Fname, Lastname=Lname, AdmissionNum=AdmissionNum, DOB=Dob, Gender=Gender,
            Std=Std, Division=Division, Religion=Religion, Blood=Bld, Contact=Contact,
            Subject=Subject, JoinDate=Joindate, WorkExperience=WorkExperience, Salary=Salary)

    allteachers = AdminUser.objects.filter(is_teacher=True)
    return render(request, 'Administration/AddTeachers.html', {'teachers': allteachers})


def ApproveTeachers(request):
    return render(request, 'Administration/ApproveTeachers.html')


def Teacherssalary(request):
    return render(request, 'Administration/Teacherssalary.html')


def AddStudents(request):
    if request.method == "POST":

        Name = request.POST["name"]
        Fname = request.POST["fname"]
        Lname = request.POST["lname"]
        Dob = request.POST["dob"]
        Gender = request.POST["gender"]
        AdmissionNum = request.POST["admnum"]
        Std = request.POST["std"]
        Division = request.POST["division"]
        Religion = request.POST["religion"]
        Bld = request.POST["bld"]
        Rollnum = request.POST["roll"]
        Contact = request.POST["contact"]

        user = AdminUser.objects.get(username=Name)
        AdminUser.objects.filter(id=user.id).update(
            Name=Name, Firstname=Fname, Lastname=Lname, AdmissionNum=AdmissionNum, DOB=Dob, Gender=Gender,
            Std=Std, Division=Division, Religion=Religion, Blood=Bld, RollNumber=Rollnum, Contact=Contact)
        print(Name)
        print(Dob)
        print(Gender)
        print(AdmissionNum)
        print(Std)
        print(Division)
        print(Contact)
        print(Rollnum)
        # student_data.save()
    allstudents = AdminUser.objects.filter(is_student=True)
    return render(request, 'Administration/AddStudents.html', {'students': allstudents})


def ApproveStudents(request):
    allstudents = AdminUser.objects.filter(is_student=True)
    return render(request, 'Administration/ApproveStudents.html', {'students': allstudents})


def ApproveStd(request, StudentId):
    AdminUser.objects.filter(id=StudentId).update(is_approved=True)
    print(id.is_approved)
    print("Approved")
    allstudents = AdminUser.objects.filter(is_student=True)
    return render(request, 'Administration/ApproveStudents.html', {'students': allstudents})


def FeeofStudents(request):
    return render(request, 'Administration/FeeofStudents.html')


def ViewAttendance(request):
    return render(request, 'Administration/ViewAttendance.html')


def signup(request):
    if request.method == 'POST':
        uname = request.POST["uname"]
        email = request.POST["email"]
        password = request.POST["password"]
        if AdminUser.objects.filter(username=uname).exists():
            messages.info(request, 'Username already used')
            # return redirect('signup')

            return render(request, 'Administration/signup.html')

        elif AdminUser.objects.filter(email=email).exists():
            messages.info(request, 'Email already used')
            # return redirect('signup')
            return render(request, 'Administration/signup.html')
        else:
            user_data = AdminUser.objects.create_user(
                username=uname, email=email, password=password, is_admin=True)
            user_data.save()
            # return redirect('AdminLogin')
            return render(request, 'Administration/AdminLogin.html')
    else:
        return render(request, 'Administration/signup.html')


def AdminLogin(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['password']
        user = authenticate(request, username=uname, password=password)
        if user is not None and user.is_admin:
            # print(user,uname,password)
            login(request, user)
            # return redirect("dashboard")
            return render(request, 'Administration/dashboard.html')
        else:
            # print(user,uname,password)
            messages.info(request, 'Invalid Username or Password')
            # return redirect('AdminLogin')
            return render(request, 'Administration/AdminLogin.html')
    else:
        return render(request, 'Administration/AdminLogin.html')

    # return render(request, 'Administration/AdminLogin.html')


def Adminlogout(request):
    logout(request)
    return render(request, 'Administration/index.html')
