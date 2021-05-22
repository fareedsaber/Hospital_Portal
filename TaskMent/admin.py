from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Department)
admin.site.register(Section)
admin.site.register(TaskOwner)
admin.site.register(TaskSituation)
admin.site.register(MonitoringTool)
admin.site.register(FollowUpFrequency)
admin.site.register(Tasks)
