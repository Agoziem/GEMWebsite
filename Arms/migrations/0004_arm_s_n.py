# Generated by Django 2.2 on 2023-06-23 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arms', '0003_auto_20230607_0631'),
    ]

    operations = [
        migrations.AddField(
            model_name='arm',
            name='S_N',
            field=models.IntegerField(default=1),
        ),
    ]
