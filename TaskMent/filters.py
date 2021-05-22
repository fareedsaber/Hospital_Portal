import django_filters
from .models import *


class TaskFilter(django_filters.FilterSet):
    # DepName = django_filters.CharFilter(lookup_expr='iexact')
    # sec = django_filters.CharFilter(lookup_expr='iexact')
    # TaskOwner = django_filters.CharFilter(lookup_expr='iexact')
    # Status = django_filters.CharFilter(lookup_expr='iexact')
    # TaskDate = django_filters.CharFilter(lookup_expr='iexact')
    # DueDate = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Tasks
        fields =   ['DepName','TaskOwner','Status','TaskSituation']
        
