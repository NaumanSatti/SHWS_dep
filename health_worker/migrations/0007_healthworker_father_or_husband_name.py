# Generated by Django 3.2 on 2022-03-26 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_worker', '0006_healthworker_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthworker',
            name='father_or_husband_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]