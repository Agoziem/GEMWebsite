# Generated by Django 2.2 on 2023-06-12 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_auto_20230608_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='GEM_Arm',
            field=models.CharField(choices=[('Bible Studies', 'Bible Studies'), ('Revival Prayers', 'Revival Prayers'), ('Foundation', 'Foundation'), ('Women', 'Women'), ('Partners', 'Partners')], default='None', max_length=300),
        ),
    ]