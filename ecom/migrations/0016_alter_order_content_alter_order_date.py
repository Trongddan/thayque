# Generated by Django 4.0.4 on 2022-05-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0015_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='content',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
