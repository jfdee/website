# Generated by Django 3.1.2 on 2020-10-26 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201026_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='image_height',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='image_width',
        ),
        migrations.AlterField(
            model_name='developer',
            name='image',
            field=models.ImageField(default='defaultPicture', upload_to='images/', verbose_name='Картинка'),
        ),
    ]
