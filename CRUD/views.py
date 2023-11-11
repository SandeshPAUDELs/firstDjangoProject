# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import redirect, render
# # from django.templatetags.static import static
# from .models import Employees


# def homePage(request):  
#     emp = Employees.objects.all()
#     for i in emp:
#         print(i.name)
#         print(i.email)
#         print(i.address)
#         print(i.phone)
#     context = {
#         'emp': emp,
#     }
#     return render(request, "index.html", context)

