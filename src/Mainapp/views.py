from django.shortcuts import render
from django.http import HttpResponse
from .forms import inputform as inputform1

# Create your views here.
def home(request):
	return render(request,"index.html",{})
def forminput(request):
	if request.method=='POST':
                print(request.POST)
		inputform = inputform1(request.POST)
		if inputform.is_valid():
                        print('Hello')
                        print(inputform.cleaned_data)
			ML(inputform.cleaned_data)
		else:
			#render error  page here
                        print('Error')
			return render(request,"error.html",{})
	
	#render the index page here
	return render(request,"index.html",{})

def ML(data):
	#handle it from here
	pass
