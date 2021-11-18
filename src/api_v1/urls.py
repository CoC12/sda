from django.urls import path
from .views import stream_data_view


urlpatterns = [
    path('metrics/<str:metrics_code>/data', stream_data_view, name='register_stream_data'),
]
