# Generated by Django 3.2.4 on 2021-11-29 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuardianArea', '0044_alter_guardiandetails_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='Phone',
            field=models.CharField(blank=True, default='+8801', max_length=20, null=True),
        ),
    ]