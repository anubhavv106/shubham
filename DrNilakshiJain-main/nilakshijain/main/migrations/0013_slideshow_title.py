# Generated by Django 4.1.3 on 2023-05-05 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_rename_img_slideshow_img_rename_img1_slideshow_img1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideshow',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]