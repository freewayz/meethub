# Generated by Django 2.0.4 on 2018-04-28 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20180427_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='details',
            field=models.TextField(max_length=1000),
        ),
    ]
