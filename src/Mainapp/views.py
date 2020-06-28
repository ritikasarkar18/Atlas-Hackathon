from django.shortcuts import render
from django.http import HttpResponse
# from .forms import inputform as inputform1

# Create your views here.
def home(request):
    return render(request,"index.html",{})
def forminput(request):
    if request.method=='POST':
        dic = dict(request.POST)
        fl = request.FILES 
        ML(int(dic['style'][0]), dic['color'][0], float(dic['slider'][0]),fl['pdf']) 
    return render(request,"index.html",{})

def ML(style, color, thickness, fl):
    print(style)
    print(color)
    print(thickness)
    print(fl)
