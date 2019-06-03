from django.db.models.signals import post_save
#post_save is a signal that is fired when an object is save ,
# and gives us ability to perform some tasks if we need to perform after something happens.
#for example if a user register ,a profile should be created automatically 
# for that user rather than going to admin panel and creating a profile for that new user

from django.contrib.auth.models import User
#User model is the sender that sends the signal when a new user is saved


#a receiver is a function that performs some operation when receives a signal
from django.dispatch import receiver
from .models import Profile
# a receiver decorator take 2 args, type of 
#signal and sender of that signal
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()      

#now we need to import the signals in users -> apps.py in ready function    