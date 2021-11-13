# Generated by Django 3.2.3 on 2021-11-13 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Metrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='名前')),
                ('code', models.CharField(max_length=128, verbose_name='コード')),
                ('description', models.TextField(blank=True, null=True, verbose_name='説明')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザ')),
            ],
        ),
        migrations.CreateModel(
            name='StreamData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='日時')),
                ('value', models.DecimalField(decimal_places=4, max_digits=16, verbose_name='値')),
                ('metrics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analytics.metrics', verbose_name='メトリクス')),
            ],
        ),
    ]
