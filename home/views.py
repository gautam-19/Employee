from django.shortcuts import render, HttpResponse
from home.models import Employee
from datetime import datetime


# Create your views here.
def index(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        id_no = request.POST.get('id_no')
        dept = request.POST.get('dept')
        salary = request.POST.get('salary')
        
        index = Employee(first_name=first_name, last_name=last_name, email=email, phone=phone, id_no=id_no, dept=dept, salary=salary, date=datetime.today())
        index.save()

    return render(request, 'index.html')

def all(request):
    emps = Employee.objects.all()
    context = { 'emps': emps } 
    print(context)
    return render(request, 'all.html', context)

def remove(request, id_no=0):
    if id_no:
        try:
            # Try to retrieve the employee with the given id_no
            emp_to_be_removed = Employee.objects.get(id_no=id_no)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully!")
        except Employee.DoesNotExist:
            # Handle case where employee with id_no does not exist
            return HttpResponse("Employee not found.")

    # If id_no is not provided or deletion fails, retrieve all employees and render remove.html
    emps = Employee.objects.all()
    context = { 'emps': emps } 
    return render(request, 'remove.html', context)

def filter(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dept = request.POST.get('dept')
        emps = Employee.objects.all()
        if first_name:
            emps = emps.filter(first_name=first_name)
        if last_name:
            emps = emps.filter(last_name=last_name)
        if dept:
            emps = emps.filter(dept=dept)
        
        context = {
            'emps':emps
        }
        return render(request,'all.html', context)
    elif request.method == 'GET':
        return render(request, 'filter.html')

def contact(request):
    return render(request, 'contact.html')
