# Generated by Django 3.2.4 on 2021-11-28 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0079_auto_20211111_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thana',
            name='District',
            field=models.ForeignKey(default=74, on_delete=django.db.models.deletion.CASCADE, to='Teacher.district'),
        ),
    ]