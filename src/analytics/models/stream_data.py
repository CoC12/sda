from django.db import models


class StreamData(models.Model):
    datetime = models.DateTimeField(
        verbose_name='日時',
    )
    value = models.DecimalField(
        verbose_name='値',
        decimal_places=4,
        max_digits=16,
    )
    metrics = models.ForeignKey(
        'Metrics',
        verbose_name='メトリクス',
        on_delete=models.CASCADE,
    )
