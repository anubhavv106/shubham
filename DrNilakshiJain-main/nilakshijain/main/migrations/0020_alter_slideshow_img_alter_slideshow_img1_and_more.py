# Generated by Django 4.1.6 on 2023-05-30 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_slideshow_img_alter_slideshow_img1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideshow',
            name='img',
            field=models.ImageField(upload_to='static/uploads'),
        ),
        migrations.AlterField(
            model_name='slideshow',
            name='img1',
            field=models.ImageField(upload_to='static/uploads'),
        ),
        migrations.AlterField(
            model_name='slideshow',
            name='img2',
            field=models.ImageField(upload_to='static/uploads'),
        ),
        migrations.AlterField(
            model_name='slideshow',
            name='img3',
            field=models.ImageField(upload_to='static/uploads'),
        ),
        migrations.AlterField(
            model_name='slideshow',
            name='img4',
            field=models.ImageField(upload_to='static/uploads'),
        ),
        migrations.AlterField(
            model_name='slideshow',
            name='img5',
            field=models.ImageField(upload_to='static/uploads'),
        ),
    ]
