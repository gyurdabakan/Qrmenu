# Generated by Django 3.2.7 on 2022-03-15 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_home',
            field=models.BooleanField(default=False),
        ),
    ]
