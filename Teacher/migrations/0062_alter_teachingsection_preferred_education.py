# Generated by Django 3.2.4 on 2021-10-17 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0061_teacher_ielts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachingsection',
            name='Preferred_Education',
            field=models.SmallIntegerField(choices=[(0, 'Nursery/Play/KG'), (1, 'Class 1'), (2, 'Class 2'), (3, 'Class 3'), (4, 'Class 4'), (5, 'Class 5'), (6, 'Class 6'), (7, 'Class 7'), (8, 'Class 8'), (9, 'Class 9'), (10, 'Class 10'), (11, 'Class 11'), (12, 'Class 12'), (20, 'Others')], default=20),
        ),
    ]