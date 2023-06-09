# Generated by Django 2.2 on 2023-04-13 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=300)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_Flier', models.ImageField(upload_to='assets/Events')),
                ('Title', models.CharField(max_length=300)),
                ('description', models.TextField(help_text='max_lenght of 300', max_length=300)),
                ('Day', models.CharField(max_length=300)),
                ('Month', models.CharField(max_length=300)),
                ('Time', models.CharField(max_length=300)),
                ('Zoom_meeting', models.BooleanField(default=True)),
                ('Zoom_ID', models.CharField(max_length=300)),
                ('Zoom_Password', models.CharField(max_length=300)),
                ('Other_Venue', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Organization_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('Vision', models.TextField()),
                ('Mission', models.TextField()),
                ('About', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Picture', models.ImageField(upload_to='assets/Photogallery')),
                ('description', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=300)),
                ('Picture', models.ImageField(upload_to='assets/Projects')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profileimage', models.ImageField(upload_to='assets/Profile')),
                ('Name', models.CharField(max_length=300)),
                ('Responsibility', models.CharField(max_length=300)),
                ('facebook', models.CharField(max_length=300)),
                ('whatsapp', models.CharField(max_length=300)),
                ('instagram', models.CharField(max_length=300)),
                ('twitter', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Value_heading', models.CharField(max_length=300)),
                ('Value', models.CharField(max_length=300)),
                ('Organization_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='Home.Organization_detail')),
            ],
        ),
    ]
