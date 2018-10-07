from django.shortcuts import render
from .import models
from .forms import User,Postform,Profuser,Createprofuser
from .models import CreateUser,Post,Users

def message(request):
	created=False
	if request.method=='GET':
		form=User()
		return render(request,'message.html',{'form':form,'created':created})
	elif request.method=='POST':
		form=User(request.POST)
		if form.is_valid():
			nm=form.cleaned_data.get('Name')
			mobno=form.cleaned_data.get('Mobile_Number')
			sub=form.cleaned_data.get('Subject')
			msg=form.cleaned_data.get('Your_message')
			User1=CreateUser(Name=nm,Mobile_Number=mobno,Subject=sub,Your_message=msg)
			User1.save()
			print("user has been created")
			created=True
			return render(request,'index.html',{'created':created})
		else:
			return render(request,'message.html',{'form':form})
# Create your views here.
def login(request):
	logged_in=False
	if request.method=='GET':
		form=Profuser()
		request.session['logged_in']=logged_in
		accepted=True
		return render(request,'login.html',{'form':form,'logged_in':logged_in,'accepted':accepted})
	elif request.method=='POST':
		form=Profuser(request.POST)
		if form.is_valid():
			passwd=form.cleaned_data.get('password')
			usernm=form.cleaned_data.get('username')
			accepted=True
			try:
				user1=Users.objects.get(username=usernm)
				if user1.password==passwd:
					print('found')
					request.session['usernm']=usernm
					logged_in=True
					request.session['logged_in']=logged_in
					messages=CreateUser.objects.all()
					return render(request,'help.html',{'accepted':accepted,'logged_in':logged_in,'messages':messages})
					#return render(request,'home.html',{'userid':userid,'accepted':accepted})
				else:
					accepted=False
					return render(request,'login.html',{'form':form,'accepted':accepted,'logged_in':logged_in})
			except:
				accepted=False
				return render(request,'login.html',{'form':form,'accepted':accepted,'logged_in':logged_in})
		else:
			accepted=False
			return render(request,'login.html',{'form':form,'accepted':accepted,'logged_in':logged_in})


def signup(request):
	if request.method=='GET':
		method=False
		form=Createprofuser()
		return render(request,'signup.html',{'form':form,'method':method})
	elif request.method=='POST':
		form=Createprofuser(request.POST)
		method=True
		if form.is_valid():
			Fnm=form.cleaned_data.get('Full_name')
			passwd=form.cleaned_data.get('password')
			usernm=form.cleaned_data.get('username')
			cnfpasswd=form.cleaned_data.get('confirm_password')
			user=False
			if passwd==cnfpasswd:
				val=True
				print("valid form")
				try:
					user2=Users.objects.get(username=usernm)
					user=True
					return render(request,'signup.html',{'val':val,'form':form,'method':method,'user':user})
				except:
					user1=Users(username=usernm,password=passwd,Full_name=Fnm)
					user1.save()
					logged_in=True
					messages=CreateUser.objects.all()
					return render(request,'help.html',{'val':val,'logged_in':logged_in,'messages':messages})
			else:
				val=False
				return render(request,'signup.html',{'val':val,'form':form,'method':method})

def newpost(request):
	display=False
	if request.method=='GET':
		created=False
		form=Postform()
		return render (request,'post.html',{'form':form,'created':created,'display':display})
	elif request.method=='POST':
		form=Postform(request.POST)
		if form.is_valid():
			auth=form.cleaned_data.get('author')
			tit=form.cleaned_data.get('title')
			txt=form.cleaned_data.get('text')
			Post1=Post(author=auth,title=tit,text=txt)
			Post1.save()
			Posts=Post.objects.all()
			print("Post has been created")
			created=True
			return render(request,'index.html',{'created':created,'Posts':Posts,'display':display})
		else:
			return render (request,'post.html',{'form':form,'created':created,'display':display})

def logout(request):
	logged_in=False
	request.session['logged_in']
	created=False
	if request.method=='GET':
		form=User()
		return render(request,'message.html',{'form':form,'created':created})
	elif request.method=='POST':
		form=User(request.POST)
		if form.is_valid():
			nm=form.cleaned_data.get('Name')
			mobno=form.cleaned_data.get('Mobile_Number')
			sub=form.cleaned_data.get('Subject')
			msg=form.cleaned_data.get('Your_message')
			User1=CreateUser(Name=nm,Mobile_Number=mobno,Subject=sub,Your_message=msg)
			User1.save()
			print("user has been created")
			created=True
			return render(request,'message.html',{'created':created})
		else:
			return render(request,'message.html',{'form':form})

		

def post(request):
	if request.method=='GET':
		display=True
		Posts=Post.objects.all()
		return render (request,'index.html',{'Posts':Posts,'display':display})

def youth(request):
		return render (request,'youth.html')

def faq(request):
		return render (request,'faq.html')

def disaster(request):
		return render (request,'diaster.html')

def gay(request):
		return render (request,'gay.html')

def fact(request):
		return render (request,'fact.html')



 