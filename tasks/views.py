from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Home page - working!")


def register_view(request):
    return HttpResponse("Register page - working!")


def login_view(request):
    return HttpResponse("Login page - working!")


def logout_view(request):
    return HttpResponse("Logged out - working!")


def dashboard(request):
    return HttpResponse("Dashboard - working!")


def task_list(request):
    return HttpResponse("Task list - working!")


def task_create(request):
    return HttpResponse("Task create - working!")


def task_detail(request, pk):
    return HttpResponse(f"Task detail {pk} - working!")


def task_edit(request, pk):
    return HttpResponse(f"Task edit {pk} - working!")


def task_delete(request, pk):
    return HttpResponse(f"Task delete {pk} - working!")