# Generated by Django 3.0.3 on 2020-03-17 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('token_blacklist', '0007_auto_20171017_2214'),
        ('auth_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyBlacklistedToken',
            fields=[
            ],
            options={
                'verbose_name': 'отозванный токен',
                'verbose_name_plural': 'токены (отозванные)',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('token_blacklist.blacklistedtoken',),
        ),
        migrations.CreateModel(
            name='ProxyOutstandingToken',
            fields=[
            ],
            options={
                'verbose_name': 'токен',
                'verbose_name_plural': 'токены',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('token_blacklist.outstandingtoken',),
        ),
    ]
