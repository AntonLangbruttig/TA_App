from django.shortcuts import render, redirect
from django.views import View
from .models import User, Course
from Classes.functions import *


# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        result = login(request.POST['name'], request.POST['password'])
        if not result:
            return render(request, "login.html", {"message": "information is incorrect"})
        else:
            request.session["name"] = request.POST['name']
            return redirect('/SupHome/')

class SupHome(View):
    def get(self, request):
        return render(request, "sup_home.html", {})


class SupAccounts(View):
    def get(self, request):
        accounts = list(User.objects.all())
        return render(request, "sup_accounts.html", {"roles": Roles.choices, "accounts": accounts})

    def post(self, request):
        message = createAccount(request.POST['username'], request.POST['password'], request.POST['email'], request.POST['role'])
        accounts = list(User.objects.all())
        return render(request, "sup_accounts.html", {"roles": Roles.choices, "accounts": accounts, "message": message})


class RegisterCourses(View):
    def get(self, request):
        return render(request, "register_courses.html")

    def post(self, request):
        message = createCourse(request.POST['cor_id'], request.POST['cor_name'], request.POST['cor_sched'], request.POST['cor_cred'])
        return render(request, "register_courses.html", {"message": message})

class SupEmail(View):
    def get(self, request):
        return render(request, "sup_email.html", {})


class Account(View):
    def get(self, request):
        return render(request, "account.html", {})

class SupCourses(View):
    def get(self, request):
        courses = list(Course.objects.all())
        return render(request, "sup_courses.html", {"courses":courses})

    def post(self, request):
        Course.objects.get(courseid=request.POST["delete_course"]).delete()
        courses = list(Course.objects.all())
        return render(request, "sup_courses.html", {"courses": courses})

class CreateLab(View):
    def get(self,request):
        return render(request, "sup_create_lab.html")



