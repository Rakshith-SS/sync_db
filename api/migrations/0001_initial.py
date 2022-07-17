# Generated by Django 4.0.6 on 2022-07-17 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('level', models.IntegerField()),
                ('stars', models.DecimalField(decimal_places=1, max_digits=2)),
                ('gameType', models.CharField(max_length=15)),
                ('duration', models.DateTimeField()),
                ('timestamp', models.DecimalField(decimal_places=7, max_digits=17)),
                ('sync', models.BooleanField(default=False)),
                ('isActive', models.BooleanField(default=False)),
            ],
        ),
    ]