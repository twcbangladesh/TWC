# Generated by Django 3.2.4 on 2021-10-10 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0052_ssc_hsc_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='BAN',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]