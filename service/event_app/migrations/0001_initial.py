# Generated by Django 4.2.7 on 2023-12-03 20:16

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
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128)),
                ('phone_number', models.CharField(max_length=11)),
                ('social_links', models.CharField(max_length=128)),
                ('organization', models.CharField(max_length=128)),
                ('event_name', models.CharField(max_length=128)),
                ('event_type', models.CharField(max_length=128)),
                ('event_date', models.CharField(max_length=12)),
                ('event_time', models.CharField(max_length=5)),
                ('event_place', models.CharField(max_length=128)),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserEventRel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_app.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
