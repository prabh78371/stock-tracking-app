# Generated by Django 4.0.2 on 2022-04-15 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_tracking_app', '0002_stock_tracking_model_barcode_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Barcode', models.IntegerField()),
                ('product_code', models.IntegerField()),
                ('no_of_cartons', models.IntegerField()),
                ('barcode_image', models.ImageField(blank=True, upload_to='images/')),
                ('Timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='stock_tracking_model',
            name='Timestamp',
        ),
        migrations.RemoveField(
            model_name='stock_tracking_model',
            name='barcode_image',
        ),
    ]
