# Generated by Django 3.2.4 on 2021-08-28 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GuardianArea', '0021_alter_child_slug'),
        ('FollowUp', '0007_permanenttuitionforchild_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortlistedtuitionforchild',
            name='Child',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='GuardianArea.child', unique=True),
        ),
    ]