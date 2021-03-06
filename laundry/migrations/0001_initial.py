# Generated by Django 4.0.4 on 2022-05-24 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laundry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='LaundryEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('day', models.DateField()),
                ('laundry', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='entries', to='laundry.laundry')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='entries', to='users.user')),
            ],
        ),
    ]
