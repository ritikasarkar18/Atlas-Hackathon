from django.shortcuts import render
from django.http import HttpResponse
import time
from atlas import settings
# from .forms import inputform as inputform1

def forminput(request):
    if request.method=='POST':
        dic = dict(request.POST)
        fl = request.FILES 
        request.session['hello'] =[int(dic['style'][0]), dic['color'][0], float(dic['slider'][0])] 
        settings.pdf_file = fl
        return render(request, "loading.html", {'load' : True})
    return render(request,"index.html",{})

def ML(request):
    data = request.session.get('hello')
    style = data[0]
    color = data[1]
    thickness = data[2]
    fl = settings.pdf_file['pdf']
    time.sleep(5)
    return render(request, "loaded.html", {'Text' : "loaded"})
