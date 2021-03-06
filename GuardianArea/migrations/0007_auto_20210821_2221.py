# Generated by Django 3.2.4 on 2021-08-21 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuardianArea', '0006_auto_20210821_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='Note',
            field=models.ManyToManyField(blank=True, null=True, to='GuardianArea.Note'),
        ),
        migrations.AlterField(
            model_name='child',
            name='slug',
            field=models.SlugField(default='8c81', help_text='Do not change it', max_length=5, primary_key=True, serialize=False),
        ),
    ]
