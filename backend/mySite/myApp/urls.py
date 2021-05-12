"""mySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# url patterns
urlpatterns = [

    # default root
    path('', views.index, name="dashboard"),

    # add class
    path('addclass',
         views.student_classes_create, name="createClass"),

    # Class list
    path('classlist',
         views.student_classes_manage, name="manageClass"),

    # manage class
    path('updatelist', views.student_classes_update, name="updateClass"),

    # signup
    path('signup', views._signup, name="signup"),

    # login
    path('login', views._login, name="login"),

    # recover password
    path('forgotpassword', views.recover_password, name="forgotpassword"),

    # change password
    path('resetpassword', views.reset_password, name="resetpassword"),

    # add student
    path('addstudent', views.add_student, name="addstudent"),

    # manage student
    path('managestudent', views.manage_student, name="managestudent"),

    # edit student
    path('editstudent', views.edit_student, name="editstudent"),

    # add result
    path('addresult', views.add_result, name="addresult"),

    # show result
    path('showresult', views.show_result, name="showresult"),

    # time table
    path('timetable', views.time_table, name="Timetable"),

    # change time table
    path('changetimetable', views.change_time_table, name="changeTimetable"),

    # add subject
    path('createsubject', views.add_subject, name="createsubject"),

    # manage subject
    path('managesubject', views.manage_subject, name="managesubject"),

    # edit subject
    path('editsubject', views.edit_subject, name="editsubject"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # media folder
