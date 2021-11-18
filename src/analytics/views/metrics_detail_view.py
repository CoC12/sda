from django.urls import reverse
from django.views.generic import UpdateView
from ..models import Metrics


class MetricsDetailView(UpdateView):
    template_name = 'analytics/metrics_detail.html'
    model = Metrics
    fields = (
        'title',
        'code',
        'description',
    )

    def get_form(self):
        form = super().get_form()
        form.fields['code'].widget.attrs['readonly'] = 'readonly'
        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'
        return form

    def get_success_url(self):
        return reverse('metrics_detail', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.code = self.get_object().code
        object.save()
        return super().form_valid(form)

metrics_detail_view = MetricsDetailView.as_view()
