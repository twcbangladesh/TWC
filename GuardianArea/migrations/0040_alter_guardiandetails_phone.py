# Generated by Django 3.2.4 on 2021-11-28 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuardianArea', '0039_auto_20211003_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guardiandetails',
            name='Phone',
            field=models.CharField(default='+8801', max_length=20),
        ),
    ]