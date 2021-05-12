from django.shortcuts import render
# from .models import signup, TimeTable, StudentClass

# Create your views here.

########## Home Page #########

# dashboard


def index(request):
    # getting all data from db
    # user = signup.objects.all()[1]
    # total registered users
    # count = signup.objects.all().count
    # , {'user': user, 'count': count}
    return render(request, 'dashboard/index.html')

########### student classes ##########

# create class


def student_classes_create(request):
    # if request.method == "POST":
    #     name =  request.POST["className"]
    #     num = request.POST["classNum"]
    #     sec = request.POST["classSec"]      
    #     # print(name, num, sec)
    #     class_ = StudentClass(className=name, classNum=num, classSec=sec)
    #     class_.save()
    #     print("data saved")
    return render(request, 'studentClasses/CreateClass.html')
# manage class


def student_classes_manage(request):
    return render(request, 'studentClasses/ManageClass.html')
# update class


def student_classes_update(request):
    return render(request, 'studentClasses/UpdateClass.html')

########## User Authentication ##########

# signup


def _signup(request):
    return render(request, 'user/Signup/signup.html')

# login


def _login(request):
    return render(request, 'user/Login_v2/index.html')

# recover password


def recover_password(request):
    return render(request, 'user/forgotpassword.html')

# change password


def reset_password(request):
    return render(request, 'user/reset/reset.html')


########### Time Table ###########

# time table
def time_table(request):
    # fetch all timetable columns
    # tt = TimeTable.objects.all()
    # , {'tt': tt}
    return render(request, 'timetable/index.html')

# change time table


def change_time_table(request):
    return render(request, 'timetable/change_timetable.html')

########## Student ##########

# add student


def add_student(request):
    return render(request, 'student/addStudent.html')

# manage student


def manage_student(request):
    return render(request, 'student/manageStudent.html')

# update student

def edit_student(request):
	return render(request, 'student/updatestudent.html')

########## Result ##########

# add result


def add_result(request):
    return render(request, 'result/result-1.html')

# show result


def show_result(request):
    return render(request, 'result/result-2.html')

########### Subject  ############

# create subject


def add_subject(request):
    return render(request, 'subject/createSubject.html')

# manageSubject


def manage_subject(request):
    return render(request, 'subject/ManageSubject.html')

# edit subject

def edit_subject(request):
    return render(request, 'subject/Edit.html')