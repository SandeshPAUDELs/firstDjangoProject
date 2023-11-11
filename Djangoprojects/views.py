# from django.http import HttpResponse
from django.shortcuts import render
# from django.templatetags.static import static
from CRUD.models import *


def homePage(request):  
    emp = Employees.objects.all()

    data = {
        "emp": emp,
    }
  
    return render(request, "index.html", data)


