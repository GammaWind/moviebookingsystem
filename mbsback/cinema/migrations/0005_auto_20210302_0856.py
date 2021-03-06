# Generated by Django 3.1.7 on 2021-03-02 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
        ('cinema', '0004_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='cinemahall_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cinema.cinemahall'),
        ),
        migrations.AddField(
            model_name='show',
            name='movie_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='movie.movie'),
        ),
        migrations.AlterField(
            model_name='cinemahall',
            name='cinama_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cinema.cinema'),
        ),
        migrations.AlterField(
            model_name='cinemasincity',
            name='cinema_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cinema.cinema'),
        ),
        migrations.AlterField(
            model_name='cinemasincity',
            name='city_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cinema.city'),
        ),
        migrations.AlterField(
            model_name='seats',
            name='cinemahall_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cinema.cinemahall'),
        ),
    ]
