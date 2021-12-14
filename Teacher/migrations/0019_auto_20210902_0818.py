# Generated by Django 3.2.4 on 2021-09-02 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0018_auto_20210902_0801'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='HSC_MEDIUM',
            field=models.IntegerField(blank=True, choices=[(1, 'Bangla Medium'), (2, 'English Medium'), (3, 'English Version'), (4, 'Arbi Medium'), (5, 'Arbi Version'), (6, 'Technical')], null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='Post_Graduation_GPA',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='Post_Graduation_Institute',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='PG_Institute', to='Teacher.university'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='Post_Graduation_Subject',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='PG_Subject', to='Teacher.subject'),
        ),
    ]