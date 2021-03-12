# Generated by Django 3.1.7 on 2021-03-11 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cinema', '0011_auto_20210311_0708'),
        ('booking', '0006_auto_20210311_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreBooking',
            fields=[
                ('prebooking_id', models.AutoField(primary_key=True, serialize=False)),
                ('seat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.seats')),
                ('show_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cinema.show')),
                ('user_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
