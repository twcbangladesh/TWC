# Generated by Django 3.2.4 on 2021-09-14 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FollowUp', '0012_employeeloginhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Avatar',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='NID',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='Proof_Of_Presence',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
