from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):      
    return render(request, "index.html", {"course": "Django"})


def aboutUs(request):
    return HttpResponse("Welcome to world");

def aboutMe(request):
    return HttpResponse("imported Successfulllll")

def courseDetails(request, courseid):
    return HttpResponse(courseid)