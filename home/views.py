from django.shortcuts import render, HttpResponse

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
## Function to call aboutus page template
######################################
def ticket(request):
    return render(request, 's.html')

######################################
## Function to call aboutus page template
######################################
######################################
## Function to call aboutus page template
######################################
######################################
## Function to call aboutus page template
######################################
