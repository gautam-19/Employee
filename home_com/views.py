from django.shortcuts import render, HttpResponse
from home_com.models import Contact
from datetime import datetime

# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        ph = request.POST.get('ph')
        info = request.POST.get('info')

        contact = Contact(name=name, email=email,ph=ph, info=info, date= datetime.today())
        contact.save()

    return render(request, 'contact.html')

def C_home(request):
    return render(request, 'C_home.html')

def about(request):
    return render(request, 'about.html')

def job(request):
    return HttpResponse("Coming Soon!")