# Generated by Django 3.2.4 on 2021-09-08 08:41

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0033_alter_teacher_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='Phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default='+8801720274040', max_length=128, null=True, region=None),
        ),
    ]