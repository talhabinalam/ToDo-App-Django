from django.shortcuts import render, HttpResponse


def taskList(request):
    return HttpResponse("To Do list")
