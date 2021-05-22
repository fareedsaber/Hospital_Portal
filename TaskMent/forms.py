from django.forms import widgets
from django.forms.widgets import DateTimeInput
from acc import models
from django import forms
from django.contrib.auth.models import  User
from .models import *
from django.contrib.auth.forms import  UserCreationForm
from django.utils import timezone

class AddTasks(forms.ModelForm):    
       
    class Meta:
        model = Tasks
        fields=[
                        
            'user',
            'DepName',
            'sec',
                'TaskOwner',
                'TaskSituation',
                'MonitoringTool',
                'FOF',
                'Status',
                'Task',
                'TaskDate',
                'DueDate',
                'Comment'
                ]
        widgets={
       
            'DepName':forms.Select(attrs={'class':'form-control'}),
            'sec':forms.Select(attrs={'class':'form-control'}),

            'TaskOwner':forms.Select(attrs={'class':'form-control' }),
            'TaskSituation':forms.Select(attrs={'class':'form-control'}),
            'MonitoringTool':forms.Select(attrs={'class':'form-control'}),
            
            'FOF':forms.Select(attrs={'class':'form-control'}),
            'Status':forms.Select(attrs={'class':'form-control'}),
            'Task':forms.TextInput(attrs={'class':'form-control'}),
            
            'TaskDate':forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date'}),
            'DueDate':forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date'}),
            'Comment':forms.Textarea(attrs={'class':'form-control'})
        }
class AddTDep(forms.ModelForm):
    class Meta:
        model = Department
        fields=['DepName']
        widgets={
            'DepName': forms.TextInput(attrs={'class':'form-control'})
        }

class AddSectionsForm(forms.ModelForm) :    
    class Meta:
        model = Section
        fields = ['section','Dep']       
        widgets={
            'DepName':forms.TextInput(attrs={'class':'form-control'}),
            'Section':forms.TextInput(attrs={'class':'form-control'})
        }
class AddTaskOwnerForm(forms.ModelForm) :    
    class Meta:
        model = TaskOwner
        fields = ['TOName']       
        widgets={
            'TOName':forms.TextInput(attrs={'class':'form-control'}),
            
        }        
class AddTaskSituationForm(forms.ModelForm) :    
    class Meta:
        model = TaskSituation
        fields = ['SituationName']       
        widgets={
            'SituationName':forms.TextInput(attrs={'class':'form-control'}),
            
        }                
        
class AddMonitoringToolForm(forms.ModelForm) :    
    class Meta:
        model = MonitoringTool
        fields = ['SourceName']       
        widgets={
            'SourceName':forms.TextInput(attrs={'class':'form-control'}),
            
        }                
        
class AddFollowUpFrequencyForm(forms.ModelForm) :    
    class Meta:
        model = FollowUpFrequency
        fields = ['FUFName']       
        widgets={
            'FUFName':forms.TextInput(attrs={'class':'form-control'}),
            
        }                        