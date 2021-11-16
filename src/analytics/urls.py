from django.urls import path
from .views import dashboard_view, metrics_data_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('metrics_data/', metrics_data_view, name='metrics_data'),
]
