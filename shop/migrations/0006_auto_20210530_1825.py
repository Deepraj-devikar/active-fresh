# Generated by Django 3.2 on 2021-05-30 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_shop_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='area',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='contactNumber',
        ),
    ]
