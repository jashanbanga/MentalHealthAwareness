from django.db import models
from django.utils import timezone

# Create your models here.
class CreateUser(models.Model):
	Name=models.CharField(max_length=20)
	Mobile_Number=models.IntegerField()
	Subject=models.CharField(max_length=20)
	Your_message=models.CharField(max_length=200)

	def __str__(self):
		return self.Name

class Users(models.Model):
	Full_name=models.CharField(max_length=20)
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)

	def __str__(self):
		return self.username

class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    text = models.TextField()
    #created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
    	return self.author



# Create your models here.
