from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
from form.models import address
from django.contrib.auth import authenticate,login,logout
from form.forms import signups,loginform,addressform
from django.contrib import messages

# Create your views here.


def user_login(request):
	if not request.user.is_authenticated:
		if request.method=='POST':
			fm=loginform(request=request,data=request.POST)
			if fm.is_valid():
				nm=fm.cleaned_data['username']
				ps=fm.cleaned_data['password']
				user=authenticate(username=nm,password=ps)
				if user is not None:
					login(request,user)
					

					return HttpResponseRedirect('/dashboard/')
		else:
			fm=loginform()
		return render(request,'core/login.html',{'fm':fm})
	else:
		return HttpResponse('<h1>You are already Loggedin <h1>')
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/login/')


def signup(request):
	if not request.user.is_authenticated:
		if request.method=='POST':
			form=signups(request.POST)
			if form.is_valid():
				form.save()
				form=signups()
				messages.success(request,'your register successfully')

		else:
			form=signups()
		return render(request,'core/signup.html',{'fm':form})
	else:
		return HttpResponseRedirect('/dashboard/')

def dashboard(request):
	if request.user.is_authenticated:
		ads=address.objects.filter(Name=request.user)
		
		return render(request,'core/dashboard.html',{'ads':ads,'name':request.user})
	else:
		return HttpResponseRedirect('/login/')

def addaddress(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			fm=addressform(request.POST)
			if fm.is_valid():
				city=fm.cleaned_data['city']
				state=fm.cleaned_data['state']
				country=fm.cleaned_data['country']
				pin=fm.cleaned_data['pin']
				
				pst=address(city=city , state=state, country=country,pin=pin,Name=request.user,date=datetime.now())
				pst.save()
				messages.success(request," Your address successfully added")
				return HttpResponseRedirect('/dashboard/')
				
		else:
			fm=addressform()
		return render(request,'core/addaddress.html',{'fm':fm})
	else:
		return HttpResponseRedirect('/login/')

def updateaddress(request,id):
	if request.user.is_authenticated:
		if request.method=='POST':
			pi=address.objects.get(pk=id)
			fm=addressform(request.POST,instance=pi)
			if fm.is_valid():
				fm.save()
				messages.success(request," Your address successfully updated")

		else:
			pi=address.objects.get(pk=id)
			fm=addressform(instance=pi)
		return render(request,'core/updateaddress.html',{'fm':fm})
	else:
		return HttpResponseRedirect('/login/')

def deleteaddress(request,id):
	if request.user.is_authenticated:
		if request.method=='POST':
			pi=address.objects.get(pk=id)
			pi.delete()
			return HttpResponseRedirect('/dashboard/')
	else:
		return HttpResponseRedirect('/login/')