from django.contrib.auth import authenticate
from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Department, Tasks
from .forms import *
from .filters import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .decorators import *
# from acc.models import *



# Create your views here.
@login_required()
def tasks (request):     
    gettsk=Tasks.objects.filter(user=request.user) 
    Open=Tasks.objects.filter(Status='Open').count()
    compete=Tasks.objects.filter(Status='Complete').count()
    Struggling=Tasks.objects.filter(Status='Struggling').count()
    In_Progress=Tasks.objects.filter(Status='In_Progress').count() 
    searchfilter=TaskFilter(request.GET,queryset=gettsk)
    gettsk=searchfilter.qs
    
    
    context={
        'gettsk':gettsk,
        'GetAllTasks':AddTasks(),
        'Struggling':Struggling,
        'Open':Open,
        'compete':compete,
        'In_Progress':In_Progress,
        'myTaskFilter':searchfilter,
        
        }           
    return render(request,'tasks/tasks.html',context)

@login_required()
@allowedgroup(allweduser=['admin'])
def dashbord(request):
    user=User.objects.count()
    tsk=Tasks.objects.all()
    tskcount=Tasks.objects.count()
    Open=Tasks.objects.filter(Status='Open').count()
    compete=Tasks.objects.filter(Status='Complete').count()
    Struggling=Tasks.objects.filter(Status='Struggling').count()
    In_Progress=Tasks.objects.filter(Status='In_Progress').count()


    context={
        'userCount':user,
        'tsk':tsk,
        'tskcount':tskcount,
        'Struggling':Struggling,
        'Open':Open,
        'compete':compete,
        'In_Progress':In_Progress
    }
    return render(request,'index.html',{'context':context})
@login_required()
def AddTask(request):
          
    if request.method=='POST': 
             
            addtask=AddTasks(request.POST)              
            if addtask.is_valid():               
                           
              instance=addtask.save(commit=False) 
              instance.user=request.user
              instance.save()              
            return redirect('tmg:tasks')      
        
    context={
        
        'form':AddTasks()
    }
    return render(request ,'tasks/addtasks.html',context)
@login_required()
def TaskUpdate(request,pk):
    task=Tasks.objects.get(id=pk)
    form=AddTasks(instance=task)
    if request.method=="POST":
        form=AddTasks(request.POST,instance=task)
        if form.is_valid():
            ## here the add
            form.user = request.user
            form.save()
        return redirect('tmg:tasks')      
    context={
        'form':form
    }
    return render(request ,'tasks/TaskUpdate.html',context) 
@login_required()   
def deletetask(request,pk):
    task=Tasks.objects.get(id=pk)
    if request.method=="POST":
        task.delete()
        return redirect('tmg:tasks')
        
    context={
        'form':task
    }
    return render(request ,'tasks/taskdelete.html',context)  
@login_required() 
# end Tasks Operation   
@login_required()  
@allowedgroup(allweduser=['admin'])  
def AllDepartment (request):     
    getdep=Department.objects.all()
    contDep=Department.objects.count()
    context={
        'getdep':getdep,
         'contDep':contDep,
        }           
    return render(request,'tasks/Department.html',context)
@login_required()     
@allowedgroup(allweduser=['admin'])   
def AddDepartment(request):  
    
    if request.method=='POST':        
            adddep=AddTDep(request.POST)  
            if adddep.is_valid():
               adddep.save()
            return redirect('tmg:alldep')       
    context={
        
        'form':AddTDep()
    }
    return render(request ,'tasks/addtasks.html',context)   
@login_required()
@allowedgroup(allweduser=['admin']) 
def DepUpdate(request,pk):
    dep=Department.objects.get(id=pk)
    form=AddTDep(instance=dep)
    if request.method=="POST":
        form=AddTDep(request.POST,instance=dep)
        if form.is_valid():
            form.save()
        return redirect('tmg:alldep')    
    
    context={"form":form}
    return render(request,'tasks/depupdate.html',context)     
@login_required()
@allowedgroup(allweduser=['admin'])  
def Depdelete(request,pk):
    dep=Department.objects.get(id=pk)
    if request.method=="POST":
        dep.delete()
        return redirect('tmg:alldep')
    context={
        'form':dep
    }    
    return render(request,'tasks/depdelete.html',context)   
# end of Department Function
@login_required()
@allowedgroup(allweduser=['admin'])
def AllSections(request):
    getAllSections=Section.objects.all()       
    contSection=Section.objects.count()
    context={
        'getSections':getAllSections,
        'contSection':contSection
    }
    return render(request,'tasks/AllSections.html',context)
@login_required()
@allowedgroup(allweduser=['admin']) 
def AddSetions(request):    
    if request.method=='POST':             
            form=AddSectionsForm(request.POST)  
            if form.is_valid():
               form.save()
            return redirect('tmg:Setions')       
    context={
        
        'form':AddSectionsForm()
    }    
    return render(request,'tasks/AddSetions.html',context)
@login_required()
@allowedgroup(allweduser=['admin']) 
def UpdateSections(request,pk):    
    section=Section.objects.get(id=pk)
    form=AddSectionsForm(instance=section)
    if request.method=="POST":
        form=AddSectionsForm(request.POST,instance=section)
        if form.is_valid():
            form.save()
            return redirect('tmg:Setions')
        else:
            form=AddSectionsForm() 
    context={
        
        'form':form
    }              
    return render (request,'tasks/sectionsupdate.html',context)
@login_required()
@allowedgroup(allweduser=['admin']) 
def DeleteSection(request,pk):
    form=Section.objects.get(id=pk)
    if request.method=="POST":
        form.delete()
        return redirect('tmg:Setions')   
    context={
        'form':form
    }
    return render(request,'tasks/sectiondelete.html',context)
# end of Sections
@login_required()
@allowedgroup(allweduser=['admin']) 
def AllTaskOwner(request):
    getAllSections=TaskOwner.objects.all()       
    contSection=TaskOwner.objects.count()
    context={
        'getSections':getAllSections,
        'contSection':contSection
    }
    return render(request,'tasks/AllTaskOwner.html',context)
@login_required()
@allowedgroup(allweduser=['admin'])
def AddTaskOwner(request):    
    if request.method=='POST':             
            form=AddTaskOwnerForm(request.POST)  
            if form.is_valid():
               form.save()
            return redirect('tmg:AllTaskOwner')       
    context={
        
        'form':AddTaskOwnerForm()
    }    
    return render(request,'tasks/AddTaskowner.html',context)
@login_required()
@allowedgroup(allweduser=['admin']) 
def UpdateTaskOwner(request,pk):    
    section=TaskOwner.objects.get(id=pk)
    form=AddTaskOwnerForm(instance=section)
    if request.method=="POST":
        form=AddTaskOwnerForm(request.POST,instance=section)
        if form.is_valid():
            form.save()
            return redirect('tmg:AllTaskOwner')
        else:
            form=AddTaskOwnerForm() 
    context={
        
        'form':form
    }              
    return render (request,'tasks/TaskOwnerUpdate.html',context)
@login_required()
@allowedgroup(allweduser=['admin']) 
def DeleteTaskOwner(request,pk):
    form=TaskOwner.objects.get(id=pk)
    if request.method=="POST":
        form.delete()
        return redirect('tmg:AllTaskOwner')   
    context={
        'form':form
    }
    return render(request,'tasks/TaskOwnerDelete.html',context)
# end of TaskOwner
@login_required()
@allowedgroup(allweduser=['admin']) 
def AllTaskSituation(request):
    getAllSections=TaskSituation.objects.all()       
    contSection=TaskSituation.objects.count()
    context={
        'getSections':getAllSections,
        'contSection':contSection
    }
    return render(request,'tasks/AllTaskSituationr.html',context)
@login_required()
@allowedgroup(allweduser=['admin']) 
def AddTaskSituation(request):    
    if request.method=='POST':             
            form=AddTaskSituationForm(request.POST)  
            if form.is_valid():
               form.save()
            return redirect('tmg:AllTaskSituation')       
    context={
        
        'form':AddTaskSituationForm()
    }    
    return render(request,'tasks/AddTaskSituation.html',context)
@login_required()
@allowedgroup(allweduser=['admin'])
def UpdateTaskSituation(request,pk):    
    section=TaskSituation.objects.get(id=pk)
    form=AddTaskSituationForm(instance=section)
    if request.method=="POST":
        form=AddTaskSituationForm(request.POST,instance=section)
        if form.is_valid():
            form.save()
            return redirect('tmg:AllTaskSituation')
        else:
            form=AddTaskSituationForm() 
    context={
        
        'form':form
    }              
    return render (request,'tasks/UpdateTaskSituation.html',context)
@login_required()
@allowedgroup(allweduser=['admin']) 
def DeleteTaskSituation(request,pk):
    form=TaskSituation.objects.get(id=pk)
    if request.method=="POST":
        form.delete()
        return redirect('tmg:AllTaskSituation')   
    context={
        'form':form
    }
    return render(request,'tasks/TaskSituationDelete.html',context)
#end of tasksetuation
@login_required()
@allowedgroup(allweduser=['admin']) 
def AllMonitoringTool(request):
    getAllSections=MonitoringTool.objects.all()       
    contSection=MonitoringTool.objects.count()
    context={
        'getSections':getAllSections,
        'contSection':contSection
    }
    return render(request,'tasks/AllMonitoringTool.html',context)
@login_required()
@allowedgroup(allweduser=['admin'])
def AddMonitoringTool(request):    
    if request.method=='POST':             
            form=AddMonitoringToolForm(request.POST)  
            if form.is_valid():
               form.save()
            return redirect('tmg:AllMonitoringTool')       
    context={
        
        'form':AddMonitoringToolForm()
    }    
    return render(request,'tasks/addMonitoringTool.html',context)
@login_required()
@allowedgroup(allweduser=['admin'])  
def UpdateMonitoringTool(request,pk):    
    section=MonitoringTool.objects.get(id=pk)
    form=AddMonitoringToolForm(instance=section)
    if request.method=="POST":
        form=AddMonitoringToolForm(request.POST,instance=section)
        if form.is_valid():
            form.save()
            return redirect('tmg:AllMonitoringTool')
        else:
            form=AddMonitoringToolForm() 
    context={
        
        'form':form
    }              
    return render (request,'tasks/UpdateMonitoringTool.html',context)
@login_required()
@allowedgroup(allweduser=['admin']) 
def DeleteMonitoringTool(request,pk):
    form=MonitoringTool.objects.get(id=pk)
    if request.method=="POST":
        form.delete()
        return redirect('tmg:AllMonitoringTool')   
    context={
        'form':form
    }
    return render(request,'tasks/MonitoringToolDelete.html',context)
#end of FollowUpFrequency
@login_required()
@allowedgroup(allweduser=['admin']) 
def AllFollowUpFrequency(request):
    getAllSections=FollowUpFrequency.objects.all()       
    contSection=FollowUpFrequency.objects.count()
    context={
        'getSections':getAllSections,
        'contSection':contSection
    }
    return render(request,'tasks/AllFollowUpFrequency.html',context)
@login_required()
@allowedgroup(allweduser=['admin']) 
def AddFollowUpFrequency(request):    
    if request.method=='POST':             
            form=AddFollowUpFrequencyForm(request.POST)  
            if form.is_valid():
               form.save()
            return redirect('tmg:AllFollowUpFrequency')       
    context={
        
        'form':AddFollowUpFrequencyForm()
    }    
    return render(request,'tasks/AddFollowUpFrequency.html',context)
@login_required()
@allowedgroup(allweduser=['admin'])  
def UpdateFollowUpFrequency(request,pk):    
    section=FollowUpFrequency.objects.get(id=pk)
    form=AddFollowUpFrequencyForm(instance=section)
    if request.method=="POST":
        form=AddFollowUpFrequencyForm(request.POST,instance=section)
        if form.is_valid():
            form.save()
            return redirect('tmg:AllFollowUpFrequency')
        else:
            form=AddFollowUpFrequencyForm() 
    context={
        
        'form':form
    }              
    return render (request,'tasks/UpdateFollowUpFrequency.html',context)
@login_required()
@allowedgroup(allweduser=['admin']) 
def DeletFollowUpFrequency(request,pk):
    form=FollowUpFrequency.objects.get(id=pk)
    if request.method=="POST":
        form.delete()
        return redirect('tmg:AllFollowUpFrequency')   
    context={
        'form':form
    }
    return render(request,'tasks/FollowUpFrequencyDelete.html',context)



#-----------------------------
# def tasks_slug (request,slug):  
#     tsk_s=profile.objects.get(slug=slug)   
#     gettsk=Tasks.objects.all()  
#     Open=Tasks.objects.filter(Status='Open').count()
#     compete=Tasks.objects.filter(Status='Complete').count()
#     Struggling=Tasks.objects.filter(Status='Struggling').count()
#     In_Progress=Tasks.objects.filter(Status='In_Progress').count() 
#     searchfilter=TaskFilter(request.GET,queryset=gettsk)
#     gettsk=searchfilter.qs
    
#     context={
#         'tas_slug':tsk_s,
#         'gettsk':gettsk,
#         'GetAllTasks':AddTasks(),
#         'Struggling':Struggling,
#         'Open':Open,
#         'compete':compete,
#         'In_Progress':In_Progress,
#         'myTaskFilter':searchfilter,
        
#         }           
#     return render(request,'tasks/tasks_slug.html',context)
