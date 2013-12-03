from django.db import models
from django.contrib.auth.models import User, UserManager


class Department(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):  
        return self.name
    
class Game(models.Model):
    name_of_the_game = models.CharField(max_length=200)
    def __unicode__(self):  
        return self.name_of_the_game

class Info(models.Model):
	organization_name = models.CharField(max_length=200)
	user_name = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	game = models.ManyToManyField(Game)
	department = models.ManyToManyField(Department)
	def __unicode__(self):
		 return self.organization_name+ ': '+ 'user name: ' +self.user_name+ ', '+ 'password: ' + self.password


class CustomUser(User):
	department = models.ManyToManyField(Department)
	game = models.ManyToManyField(Game)
	objects = UserManager()





   


