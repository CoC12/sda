from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = 'analytics/dashboard.html'

dashboard_view = DashboardView.as_view()
