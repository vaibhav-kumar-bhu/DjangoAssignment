from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from form.models import address
from django.contrib import messages

class signups(UserCreationForm):
	password2=forms.CharField(label='password(Again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
	
	



	class Meta:
		model=User
		fields=['first_name','last_name','username','email']
		labels = {'first_name':'First Name',"last_name":'Last Name','email':'Email','username':'UserName'}

		widgets={'first_name':forms.TextInput(attrs={'class':'form-control'}),
			'last_name':forms.TextInput(attrs={'class':'form-control'}),
			'username':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.EmailInput(attrs={'class':'form-control'}),


		}

class loginform(AuthenticationForm):
	username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
	password=forms.CharField(label=('Password'),strip=False,
	widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class addressform(forms.ModelForm):
	class Meta:
		model=address
		fields=['city','state','country','pin']
		widgets={'city':forms.TextInput(attrs={'class':'form-control'}),

		'state':forms.Textarea(attrs={'class':'form-control'}),
		'country':forms.Textarea(attrs={'class':'form-control'}),
		'pin':forms.NumberInput,}