from django.urls import path
from .views import (
    dashboard_view,
    metrics_list_view,
    metrics_create_view,
    metrics_detail_view,
    metrics_data_view,
)

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('metrics/', metrics_list_view, name='metrics_list'),
    path('metrics/create/', metrics_create_view, name='metrics_create'),
    path('metrics/<int:pk>/', metrics_detail_view, name='metrics_detail'),
    path('metrics_data/', metrics_data_view, name='metrics_data'),
]
