# Generated by Django 3.2 on 2021-05-31 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20210530_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='weekDay',
            field=models.ManyToManyField(to='shop.WeekDay'),
        ),
    ]
