# Generated by Django 3.1.7 on 2021-03-02 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0003_seats'),
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('show_id', models.AutoField(primary_key=True, serialize=False)),
                ('show_name', models.CharField(max_length=50)),
                ('show_starttime', models.DateTimeField()),
                ('show_endtime', models.DateTimeField()),
            ],
        ),
    ]
