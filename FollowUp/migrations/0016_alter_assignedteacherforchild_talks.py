# Generated by Django 3.2.4 on 2021-09-19 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FollowUp', '0015_permanenttuitionforchild_reminder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignedteacherforchild',
            name='Talks',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
