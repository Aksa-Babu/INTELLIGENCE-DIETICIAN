# Generated by Django 4.1.4 on 2023-04-19 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dietapp', '0007_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='link',
        ),
        migrations.AddField(
            model_name='request',
            name='bmi',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='disease',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='height',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='weight',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dietapp.registration'),
        ),
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list', models.CharField(max_length=200)),
                ('r', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dietapp.request')),
            ],
        ),
    ]
