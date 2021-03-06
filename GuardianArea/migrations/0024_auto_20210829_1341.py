# Generated by Django 3.2.4 on 2021-08-29 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuardianArea', '0023_auto_20210829_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.DateTimeField(blank=True, null=True)),
                ('Text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='child',
            name='slug',
            field=models.SlugField(default='dxhi', help_text='Do not change it', max_length=5, primary_key=True, serialize=False),
        ),
    ]
