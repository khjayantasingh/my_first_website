from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
#Build in User class has fields like 
#email
#username
#password
#first name
#surname
    user = models.OneToOneField(User, on_delete=models.CASCADE)

#adding aditional information fields
    user_img = models.ImageField(upload_to = 'start_app/profile_pics', blank = True)
    potfolio_url = models.URLField(blank =True)
    
    def __str__(self):
#build-in in django.contrib.auth.models.User
        return self.user.username 


