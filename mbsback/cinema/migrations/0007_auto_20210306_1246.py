# Generated by Django 3.1.7 on 2021-03-06 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0006_cinemahall_city_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cinemahall',
            old_name='cinama_id',
            new_name='cinema_id',
        ),
        migrations.RemoveField(
            model_name='show',
            name='cinemahall_id',
        ),
        migrations.AddField(
            model_name='cinemahall',
            name='show_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cinema.show'),
            preserve_default=False,
        ),
    ]
