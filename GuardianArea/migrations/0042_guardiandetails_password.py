# Generated by Django 3.2.4 on 2021-11-28 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuardianArea', '0041_guardiandetails_auth'),
    ]

    operations = [
        migrations.AddField(
            model_name='guardiandetails',
            name='Password',
            field=models.CharField(default='+8801', max_length=20),
        ),
    ]