# Generated by Django 3.2.4 on 2021-10-11 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0055_auto_20211011_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='Password',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]