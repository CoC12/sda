from django.views.generic import ListView
from ..models import Metrics


class MetricsListView(ListView):
    template_name = 'analytics/metrics_list.html'
    model = Metrics

    def get_queryset(self, **kwargs):
        return super().get_queryset(**kwargs).filter(
            user=self.request.user,
        ).prefetch_related(
            'streamdata_set',
        )

metrics_list_view = MetricsListView.as_view()
