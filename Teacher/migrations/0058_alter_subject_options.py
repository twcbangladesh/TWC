# Generated by Django 3.2.4 on 2021-10-13 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0057_auto_20211011_1255'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['Title']},
        ),
    ]
