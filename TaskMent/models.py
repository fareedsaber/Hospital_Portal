from django.db import models
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Department(models.Model):
    DepName = models.CharField(max_length = 150)
    def __str__(self):
        return self.DepName
class Section(models.Model):
    section = models.CharField(max_length = 150)
    Dep=models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.section
class TaskOwner(models.Model):
    TOName = models.CharField(max_length = 150)
    def __str__(self):
        return self.TOName
class TaskSituation(models.Model):
    SituationName = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.SituationName
class MonitoringTool(models.Model):
    SourceName = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.SourceName
class FollowUpFrequency(models.Model):         
    FUFName = models.CharField(max_length = 150)
        
    def __str__(self):
            return self.FUFName

    
Status= [
    
       ('Open','Open'),
       ('In_Progress','In_Progress'),
       ('Struggling','Struggling'),
       ('Complete','Complete'),       
]

class Tasks(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE,)
    
   DepName = models.ForeignKey('Department', verbose_name=("Department"), on_delete=models.CASCADE)
   sec = models.ForeignKey(Section,verbose_name=("section"),on_delete=models.CASCADE,null=True)
    
   TaskOwner =models.ForeignKey('TaskOwner', verbose_name=("TaskOwner"), on_delete=models.CASCADE)
   TaskSituation =models.ForeignKey('TaskSituation', verbose_name=("TaskSituation"), on_delete=models.CASCADE)
   MonitoringTool =models.ForeignKey('MonitoringTool', verbose_name=("MonitoringTool"), on_delete=models.CASCADE)
   FOF =models.ForeignKey('FollowUpFrequency',verbose_name=("FollowUpFrequency"), on_delete=models.CASCADE)
   Status = models.CharField(max_length=150,choices=Status)
   Task = models.CharField(max_length=150)
   TaskDate = models.DateTimeField( default=timezone.now) 
   DueDate =  models.DateTimeField(default=timezone.now)
   Comment = models.TextField(max_length=250,null=True,blank=True)
   
    
   def __str__(self):
       return self.Task
   
   
   
   
   
 
