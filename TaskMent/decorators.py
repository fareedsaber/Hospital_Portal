from django.shortcuts import redirect

def notloggeduser1(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('tmg:dash')
        else:
            view_func(request,*args,**kwargs)
    return wrapper_func

def allowedgroup(allweduser=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group in allweduser:                                       
                return view_func(request,*args,**kwargs)                
            else:
                    return redirect('tmg:tasks')                 
        return wrapper_func 
    return decorator   

def forAdmins(view_func):
    def wrapper_function(request,*args,**kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group =='customer':
            return redirect('tmg:tasks')     
        if group =='admin':
            return view_func(request,*args,**kwargs)        
            
    return wrapper_function             
        