# Generated by Django 4.1.3 on 2023-01-22 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='link',
        ),
        migrations.RemoveField(
            model_name='project',
            name='name',
        ),
        migrations.AddField(
            model_name='project',
            name='data',
            field=models.TextField(null=True),
        ),
    ]
