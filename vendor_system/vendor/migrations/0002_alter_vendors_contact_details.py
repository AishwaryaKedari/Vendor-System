# Generated by Django 4.2.8 on 2023-12-08 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendors',
            name='contact_details',
            field=models.TextField(max_length=12, unique=True),
        ),
    ]
