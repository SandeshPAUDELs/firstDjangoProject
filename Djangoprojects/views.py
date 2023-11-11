# from django.http import HttpResponse
from django.shortcuts import render
# from django.templatetags.static import static
# from .models import Employees


def homePage(request):  
    # emp = Employees.objects.all()
    # context = {
    #     "emp": emp,
    # }
    return render(request, "index.html")


