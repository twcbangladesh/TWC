# Generated by Django 3.2.4 on 2021-09-27 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0041_auto_20210927_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='PresentArea',
        ),
        migrations.AddField(
            model_name='teacher',
            name='PresentArea',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='PresentArea', to='Teacher.areas'),
        ),
    ]