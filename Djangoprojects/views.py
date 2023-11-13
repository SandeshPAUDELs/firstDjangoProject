from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.templatetags.static import static
from CRUD.models import *


def homePage(request):  
    emp = Employees.objects.all()

    data = {
        "emp": emp,
    }
  
    return render(request, "index.html", data)

def add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")

        emp = Employees(name=name, email=email, address=address, phone=phone)
        emp.save()

        return redirect('homePage')

        # return render(request, "add.html")
    return render(request, "index.html")



def edit(request, emp_id):
    emp = Employees.objects.get(id=emp_id)

    if request.method == 'POST':
        emp.name = request.POST.get('name')
        emp.email = request.POST.get('email')
        emp.address = request.POST.get('address')
        emp.phone = request.POST.get('phone')
        emp.save()
        
        return redirect('homePage')

    context = {'emp': emp,}
    return render(request, 'edit.html', context)


def delete(request, emp_id):
    employee = Employees.objects.get(id=emp_id)

    if request.method == 'POST':
        # Handle form submission and delete the employee data
        employee.delete()
        return redirect('homePage')

    context = {'employee': employee}
    return render(request, 'delete.html', context)
