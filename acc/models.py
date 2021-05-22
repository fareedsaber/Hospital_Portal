from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.utils.text import  slugify
from django.utils import timezone
from datetime import datetime
# Create your models here.

kind=[
    ('m',"Male"),('F',"Female")
]




class profile(models.Model):  
    
    user=models.OneToOneField(User,verbose_name=_("user"),on_delete=models.CASCADE)
    FullName=models.CharField(_('Fullname'),max_length=50,blank=True,null=True)  
    Mobile = models.CharField(_(' Mobile'),max_length = 150,blank=True,null=True) 
    Address = models.CharField(_(' Mobile'),max_length = 150,blank=True,null=True)   
    
       
         
    image = models.ImageField(_("Images"),upload_to='profile',blank=True,null=True)
    slug = models.SlugField(_("slug"),max_length = 50,blank=True,null=True)
    
    # create save function slugfy 
    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.user.username)
    # Call the real save() method
        super(profile, self).save(*args,**kwargs) 
           
        class Meta:
            
             verbose_name = 'profile'

    def __str__(self):
        return '%s' %(self.user.username)

def create_profile(sender,**kwargs):
    if kwargs['created']:
        profile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User) 