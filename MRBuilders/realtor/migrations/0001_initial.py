# Generated by Django 4.2.7 on 2023-11-28 14:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio_data', models.TextField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='realtor')),
                ('top_seller', models.BooleanField(default=False)),
                ('date_hired', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]