# Generated by Django 4.0.4 on 2022-05-25 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry', '0002_alter_laundryentry_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laundryentry',
            name='day',
        ),
        migrations.AlterField(
            model_name='laundryentry',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='laundryentry',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]