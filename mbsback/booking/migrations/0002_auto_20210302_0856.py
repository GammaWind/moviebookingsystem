# Generated by Django 3.1.7 on 2021-03-02 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cinema', '0004_show'),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookedseat',
            name='user_id',
        ),
        migrations.AddField(
            model_name='bookedseat',
            name='booking_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='booking.booking'),
        ),
        migrations.AddField(
            model_name='bookedseat',
            name='seat_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cinema.seats'),
        ),
        migrations.AddField(
            model_name='booking',
            name='payment_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='booking.payment'),
        ),
        migrations.AddField(
            model_name='booking',
            name='show_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cinema.show'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
