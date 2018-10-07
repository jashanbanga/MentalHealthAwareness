
from django import forms

# Create your models here.
class User(forms.Form):
	Name=forms.CharField(max_length=20,required=True)
	Mobile_Number=forms.IntegerField(required=True)
	Subject=forms.CharField(max_length=20,required=True)
	Your_message=forms.CharField(max_length=200,required=True)

class Postform(forms.Form):
	author = forms.CharField(max_length=20)
	title = forms.CharField(max_length=200)
	text= forms.CharField(max_length=200)

class Profuser(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20,widget=forms.PasswordInput)


class Createprofuser(forms.Form):
	Full_name=forms.CharField(max_length=20)
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20,widget=forms.PasswordInput)
	confirm_password=forms.CharField(max_length=20,widget=forms.PasswordInput)
# Create your models here.
