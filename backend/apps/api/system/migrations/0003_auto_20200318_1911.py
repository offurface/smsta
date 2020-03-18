# Generated by Django 3.0.3 on 2020-03-18 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_auto_20200318_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicgroup',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата начала обучения'),
        ),
        migrations.AddField(
            model_name='academicgroup',
            name='subgroup_number',
            field=models.IntegerField(default=1, verbose_name='Номер подгруппы'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='public_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цифра факультета'),
        ),
        migrations.AlterField(
            model_name='student',
            name='form_training',
            field=models.IntegerField(choices=[(1, 'Не сокращенная'), (2, 'Сокращенная')], verbose_name='Форма обучения'),
        ),
    ]