from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):  
    data = {
        'title': 'Home',
        'bodyData': 'This is my first Django Project',
        'class': ['first', 'second', 'third'],
        'userDetails': [
            {'name': 'Rahul', 'age': 20},
            {'name': 'Rohit', 'age': 21},
            {'name': 'Raj', 'age': 22}, 
        ],
        'numbers' : [1,2,3,4,5,6,7,8,9,10],
    }    
    return render(request, "index.html", data)


def aboutUs(request):
    return HttpResponse("Welcome to world");

def aboutMe(request):
    return HttpResponse("imported Successfulllll")

def courseDetails(request, courseid):
    return HttpResponse(courseid)