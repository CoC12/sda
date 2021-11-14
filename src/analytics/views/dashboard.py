from django.views.generic import ListView
from ..models import Metrics


class DashboardView(ListView):
    template_name = 'analytics/dashboard.html'
    model = Metrics

    def get_queryset(self, **kwargs):
        return super().get_queryset(**kwargs).filter(
            user=self.request.user,
        ).prefetch_related(
            'streamdata_set',
        )

dashboard_view = DashboardView.as_view()
