# Generated by Django 3.1.7 on 2021-03-02 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210302_0538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]
