from django.urls import path
from.forms import *
from . import views
app_name='tmg'

urlpatterns = [
    
    path('',views.dashbord,name='dash'),
    path('AllTasks/' ,views.AllTasks,name='AllTasks'),

    path('tasks/' ,views.tasks,name='tasks'),
    path('addtask/',views.AddTask,name='addtask'),
    path('taskupdate/<str:pk>',views.TaskUpdate,name='taskupdate'),
    path('delete/<str:pk>',views.deletetask,name='deletetask'),
    
    path('dep/',views.AllDepartment,name='alldep'),
    path('adddep/',views.AddDepartment,name='adddep'),
    path('DepUpdate/<str:pk>',views.DepUpdate,name='DepUpdate'),
    path('Depdelete/<str:pk>',views.Depdelete,name='Depdelete'),
    
    path('Sections/',views.AllSections,name='Setions'),
    path('addsection/',views.AddSetions,name='addsection'),
    path('secupdate/<str:pk>',views.UpdateSections,name='secupdate'),
    path('Secdelete/<str:pk>',views.DeleteSection,name='Secdelete'),
    
    path('AllTaskOwner/',views.AllTaskOwner,name='AllTaskOwner'),
    path('addto/',views.AddTaskOwner,name='addto'),
    path('toupdate/<str:pk>',views.UpdateTaskOwner,name='toupdate'),
    path('todelete/<str:pk>',views.DeleteTaskOwner,name='todelete'),
    path('AllTaskSituation/',views.AllTaskSituation,name='AllTaskSituation'),
    path('TaskSituation/',views.AddTaskSituation,name='TaskSituation'),
    path('UpdateTaskSituation/<str:pk>',views.UpdateTaskSituation,name='UpdateTaskSituation'),
    path('TaskSituationdelete/<str:pk>',views.DeleteTaskSituation,name='TaskSituationdelete'),
    path('AllMonitoringTool/',views.AllMonitoringTool,name='AllMonitoringTool'),
    path('addMonitoringTool/',views.AddMonitoringTool,name='addMonitoringTool'),
    path('UpdateMonitoringTool/<str:pk>',views.UpdateMonitoringTool,name='UpdateMonitoringTool'),
    path('MonitoringTooldelete/<str:pk>',views.DeleteMonitoringTool,name='MonitoringTooldelete'),
    
    path('AllFollowUpFrequency/',views.AllFollowUpFrequency,name='AllFollowUpFrequency'),
    path('AddFollowUpFrequency/',views.AddFollowUpFrequency,name='AddFollowUpFrequency'),
    path('UpdateFollowUpFrequency/<str:pk>',views.UpdateFollowUpFrequency,name='UpdateFollowUpFrequency'),
    path('DeletFollowUpFrequency/<str:pk>',views.DeletFollowUpFrequency,name='DeletFollowUpFrequency'),
    # path('<slug:slug>/' ,views.tasks_slug,name='tasks_slug'),

]
