from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact, Ticket
# Create your views here.

######################################
## Function to call home page template
######################################
def firstFun(request):
    return render(request,'home.html')

######################################
## Function to call Documents page template
######################################

def docs(request):
    return render(request, 'docs.html')

######################################
## Function to call Call_us page template
######################################

def call_us(request):
    return render(request, 'call_us.html')

######################################
## Function to call aboutus page template
######################################
def aboutus(request):
    return render(request, 'aboutus.html')

######################################
## Function to call ticket page template
######################################
def ticket(request):
    if request.method=="POST":
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        course=request.POST.get('course')
        ticket=Ticket(fullname=fullname,email=email,phone=phone,password=password,course=course)
        ticket.save()
    return render(request, 'ticket.html')

######################################
## Function to call forms page template
######################################
def forms(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        contact=Contact(first_name=first_name,last_name=last_name,email=email,password=password,date=datetime.today())
        contact.save()
    return render(request, 'forms.html')
