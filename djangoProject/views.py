from django.http import HttpResponse
from django.shortcuts import render


def HelloWorld(requires):
    return HttpResponse("HelloWorld")


def index(requires):
    context = {"title": "天津大学", "name": "精仪学院"}
    return render(requires, "index.html", context)

def index1(requires):
    context = {"title":"天津大学","name":"精仪四室"}
    return render(requires, "index1.html")