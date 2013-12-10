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
	url = models.URLField(max_length = 200, blank = True)
	user_name = models.CharField(max_length=200, blank = True)
	password = models.CharField(max_length=200, blank = True)
	comments = models.TextField(max_length = 500, blank = True)
	game = models.ManyToManyField(Game, blank = True)
	department = models.ManyToManyField(Department, blank = True)
	def __unicode__(self):
		 return self.organization_name+ ': '+ 'user name: ' +self.user_name+ ', '+ 'password: ' + self.password


class CustomUser(models.Model):
	department = models.ManyToManyField(Department)
	game = models.ManyToManyField(Game)
	user = models.OneToOneField(User)



