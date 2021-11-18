from django.conf import settings
from django.db import models


class Metrics(models.Model):
    title = models.CharField(
        verbose_name='名前',
        max_length=128,
    )
    code = models.CharField(
        verbose_name='コード',
        max_length=128,
        unique=True,
    )
    description = models.TextField(
        verbose_name='説明',
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='ユーザ',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.title}({self.title})'
