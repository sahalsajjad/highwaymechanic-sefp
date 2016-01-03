from django import forms
from hm.models import Service
from django.contrib.auth.forms import AuthenticationForm
from hm import templatenames, methods

class LoginForm(AuthenticationForm):
	email		= forms.EmailField( widget=forms.EmailInput(attrs={'class':'form-control'}) )	
	password	= forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control'}) )

class RegisterForm(forms.Form):
	email		= forms.EmailField( widget=forms.EmailInput(attrs={'class':'form-control'}) )	
	password	= forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control'}) )
	password_again  = forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control'}) )
	
class SelectServiceForm(forms.Form):
	service		= forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control',
											    'rows':'50',
											     'cols':'100'	
							}),choices=Service.objects.values_list('id','name'))	

