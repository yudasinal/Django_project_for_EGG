from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):  
        return self.name
    
class Game(models.Model):
    department = models.ForeignKey(Department) 
    name_of_the_game = models.CharField(max_length=200)
    def __unicode__(self):  
        return self.name_of_the_game





   


