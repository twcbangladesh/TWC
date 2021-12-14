# Generated by Django 3.2.4 on 2021-09-20 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuardianArea', '0032_child_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='guardiandetails',
            name='LastAddress',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='Expected_Style',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'Home tuition'), (2, 'Group'), (3, 'Course'), (4, 'Online')], null=True),
        ),
    ]