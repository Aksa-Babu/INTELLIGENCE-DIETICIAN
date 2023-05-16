# Generated by Django 4.1.4 on 2023-04-19 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dietapp', '0005_pyramid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=20)),
                ('receiver', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=500)),
                ('link', models.URLField(null=True)),
            ],
        ),
    ]
