from django.http.response import JsonResponse
from django.views.generic import View
from ..models import Metrics
import json


class MetricsDataView(View):

    def get(self, request, *args, **kwargs):
        metrics_list = Metrics.objects.filter(
            user=request.user,
            pk__in=request.GET.getlist('metrics_id', [])
        ).prefetch_related(
            'streamdata_set',
        )
        return JsonResponse([
            {
                'x': [
                    stream_data.datetime for stream_data in metrics.streamdata_set.order_by('datetime').all()
                ],
                'y': [
                    stream_data.value for stream_data in metrics.streamdata_set.order_by('datetime').all()
                ],
            } for metrics in metrics_list
        ], safe=False)

metrics_data_view = MetricsDataView.as_view()
