# Generated by Django 3.2 on 2021-05-08 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('mrp', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('rate', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('information', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('oneLine', models.CharField(max_length=100)),
                ('shortDescription', models.TextField()),
                ('longDescription', models.TextField()),
                ('rating', models.IntegerField()),
                ('area', models.CharField(max_length=50)),
                ('contactNumber', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ShopImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field=200, upload_to='shop_image', width_field=200)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(height_field=200, upload_to='product_category_image', width_field=200)),
                ('products', models.ManyToManyField(to='shop.Product')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop')),
            ],
        ),
    ]
