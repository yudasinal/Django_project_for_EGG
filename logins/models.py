from django.db import models
from django.contrib.auth.models import User, UserManager

// Model for the department
class Department(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):  
        return self.name


// Model for the game
class Game(models.Model):
    name_of_the_game = models.CharField(max_length=200)
    def __unicode__(self):  
        return self.name_of_the_game


// Model for the information stored
class Info(models.Model):
	title = models.CharField(max_length=200, unique = True)
	url = models.URLField(max_length = 200, blank = True)
	name = models.CharField(max_length=200, blank = True)
	password = models.CharField(max_length=200, blank = True)
	comments = models.TextField(max_length = 500, blank = True)
	game = models.ManyToManyField(Game, blank = False)
	department = models.ManyToManyField(Department, blank = False)
	def __unicode__(self):
		 return self.title+ ': '+ 'user name: ' +self.name+ ', '+ 'password: ' + self.password

// Model for the custom user
class CustomUser(models.Model):
	department = models.ManyToManyField(Department)
	game = models.ManyToManyField(Game)
	user = models.OneToOneField(User)
	is_admin_approved = models.BooleanField(default=False)



