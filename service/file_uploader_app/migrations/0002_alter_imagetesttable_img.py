# Generated by Django 4.2.7 on 2023-12-08 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_uploader_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagetesttable',
            name='img',
            field=models.CharField(max_length=32768),
        ),
    ]