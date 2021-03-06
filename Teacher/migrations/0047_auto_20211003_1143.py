# Generated by Django 3.2.4 on 2021-10-03 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0046_auto_20211002_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='Experience',
            field=models.ManyToManyField(blank=True, related_name='Experience', to='Teacher.TeachingSection'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='Expertise',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='Preferred',
            field=models.ManyToManyField(blank=True, related_name='Preferred', to='Teacher.TeachingSection'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='PreferredArea',
            field=models.ManyToManyField(blank=True, to='Teacher.Areas'),
        ),
    ]
