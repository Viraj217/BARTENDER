# Generated by Django 5.2.4 on 2025-07-18 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='drink_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink_name', models.CharField(unique=True)),
                ('drink_count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
