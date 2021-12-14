# Generated by Django 3.2.4 on 2021-08-30 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0010_auto_20210830_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, default=1, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='UpzillaMunicipality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=150, null=True)),
                ('District', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Teacher.district')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='Division',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Teacher.division'),
        ),
    ]