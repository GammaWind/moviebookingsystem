# Generated by Django 3.1.7 on 2021-03-11 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0010_moviesincities'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cinemasincity',
            unique_together={('city_id', 'cinema_id')},
        ),
    ]
