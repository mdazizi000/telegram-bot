from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import  post_save


class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE ,)
    code_meli=models.CharField(max_length=16,blank=True,verbose_name='کدملی')
    phone=models.CharField(max_length=12,blank=True,verbose_name='شماره همراه')
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name='پروفایل'
        verbose_name_plural='پروفایل ها'

def save_profile_user(sender,**kwargs):
    if kwargs['created']:
        profile_user=Profile(user=kwargs['instance'])
        profile_user.save()

post_save.connect(save_profile_user,sender=User)