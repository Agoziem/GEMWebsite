# Generated by Django 2.2 on 2023-06-29 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_auto_20230623_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Month',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]