from TaskMent.models import Tasks
from django.contrib.auth import authenticate
from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from .forms import Login_Form,UpdateUserForm,UserCreationForm,UpdateProfileForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .decorators import *
from TaskMent .filters import*
from TaskMent.models  import*
from TaskMent.views  import*

# @notLoggedUsers
def User_login(request):
    if request.method=='POST':                
        log=Login_Form(request.POST)        
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not  None:
            login(request,user)
            return redirect('tmg:dash')
       
    log=Login_Form()   
    context={
        'log':log
    }    
    return render(request,'acc/Userlogin.html',context)

# @login_required()
# def UserProfile(request):    
#     return render(request,'acc/UserProfile.html')

@login_required()
def UserProfile(request):    
    user_form=UpdateUserForm(instance=request.user)
    update_profile=UpdateProfileForm(instance=request.user.profile)
    if request.method=='POST':        
        user_form=UpdateUserForm(request.POST,instance=request.user)
        update_profile=UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)

        if user_form.is_valid and update_profile.is_valid:  
            user_form.save()        
            update_profile.save()
            return redirect('tmg:dash')         
    return render(request,'acc/UserProfile.html',{'updateuser':user_form,'updateprofile':update_profile},)

# @notLoggedUsers
def SignUp(request):
    if request.user.is_authenticated:
        return redirect('tmg:dash')
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')       

                raw_password = form.cleaned_data.get('password1')               

                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('acc:ulogin')
            else:
                form = UserCreationForm()
                return render (request,'acc/Userlogin.html',{'signup':UserCreationForm})
        else:       
            return render (request,'acc/pageregister.html',{'signup':UserCreationForm})
                
   
@login_required()
def userLogout(request):
    logout(request)
    return redirect('acc:ulogin')



def tasks_slug (request,slug):  
    tsk_s=profile.objects.get(slug=slug)   
    # gettsk=Tasks.objects.all()  
    # Open=Tasks.objects.filter(Status='Open').count()
    # compete=Tasks.objects.filter(Status='Complete').count()
    # Struggling=Tasks.objects.filter(Status='Struggling').count()
    # In_Progress=Tasks.objects.filter(Status='In_Progress').count() 
    # searchfilter=TaskFilter(request.GET,queryset=gettsk)
    # gettsk=searchfilter.qs
    
    context={
        'tas_slug':tsk_s,
        # 'gettsk':gettsk,
        # 'GetAllTasks':AddTasks(),
        # 'Struggling':Struggling,
        # 'Open':Open,
        # 'compete':compete,
        # 'In_Progress':In_Progress,
        # 'myTaskFilter':searchfilter,
        
        }           
    return render(request,'tasks/tasks_slug.html',context)
