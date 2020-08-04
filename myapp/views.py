from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'myapp/home.html',{'name':'Hari'})

def base(request):
    return render(request,'base.html')

def trial(request):
    return HttpResponse('<h1>Project is live</h1>')

def profile(request):
    name='Hari'
    return render(request,'myapp/profile.html',{'name':name})