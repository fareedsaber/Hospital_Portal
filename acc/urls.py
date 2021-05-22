from django.urls import path
from . import views 


# Create your views here.
app_name='acc'
urlpatterns = [    
        path('' ,views.User_login,name='ulogin'),            
        path('logout/' ,views.userLogout,name='logout'),
        path('signup/',views.SignUp,name='signup'),
        path('UserProfile/',views.UserProfile,name='UserProfile'),        
        path('<slug:slug/',views.tasks_slug,name='tsk_slug'),        

]

