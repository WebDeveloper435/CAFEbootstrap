from django.shortcuts import render
from datetime import datetime
from home.models import contact

# Create your views here.
def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def menu(request):
    return render(request , "menu.html")
def contact(request):
    if request.method == "POST":
       name=request.POST.get("name")
       email=request.POST.get("email")
       phone=request.POST.get("phone")
       desc=request.POST.get("desc")
       contact = contact(name=name, email=email, phone=phone, desc=desc,date=datetime.today())
       contact.save()
    return render(request, "contact.html")
