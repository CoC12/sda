from django.urls import reverse
from django.views.generic import CreateView
from ..models import Metrics
import uuid


class MetricsCreateView(CreateView):
    template_name = 'analytics/metrics_create.html'
    model = Metrics
    fields = (
        'title',
        'description',
    )

    def get_form(self):
        form = super().get_form()
        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'
        return form

    def get_success_url(self):
        return reverse('metrics_list')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.user = request.user
        form.instance.code = f'metrics-{uuid.uuid4().hex[:16]}'
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

metrics_create_view = MetricsCreateView.as_view()
