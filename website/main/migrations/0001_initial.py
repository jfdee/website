# Generated by Django 3.1.2 on 2020-10-11 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('post', models.CharField(choices=[(1, 'Front-end'), (2, 'Back-end'), (3, 'Analyse')], max_length=2)),
                ('post_stage', models.CharField(choices=[(1, 'Junior'), (2, 'Middle'), (3, 'Senior')], max_length=2)),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]
