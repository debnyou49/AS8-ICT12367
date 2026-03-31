from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"index.html" )

def about(request):
    return HttpResponse("<h1>เกี่ยวกับเรา</h1>")

def form(request):
    return render(request, "form.html")

def contact(request):
    return HttpResponse("<h1>ติดต่อ</h1>")