# Generated by Django 3.2 on 2022-03-29 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_worker', '0010_auto_20220329_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='isheathcommittesformulated',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='report',
            name='iswomensupportgroupformulated',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
