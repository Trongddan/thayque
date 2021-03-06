# Generated by Django 4.0.4 on 2022-05-15 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0005_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('Order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecom.order')),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecom.product')),
            ],
        ),
    ]
