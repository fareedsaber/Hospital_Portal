from django.shortcuts import redirect

def notLoggedUsers(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('tmg:dash')
        else:
            return wrapper_func
        