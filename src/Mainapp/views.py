from django.shortcuts import render
from django.http import HttpResponse
from .forms import inputform

# Create your views here.

def forminput(request):
	if request.method=='POST':
		inputform = inputform(request.POST)
		if inputform.is_valid():
			ML(inputform.cleaned_data)
		else:
			#render error  page here
			return render(request,"error.html",{})
	else:
		inputform= inputform()
	#render the index page here
	return render(request,"index.html",{})

def ML(data):
	#handle it from here