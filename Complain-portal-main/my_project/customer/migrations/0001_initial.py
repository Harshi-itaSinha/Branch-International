# Generated by Django 5.0.1 on 2024-01-17 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('order_date', models.DateField()),
                ('product_category', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('question', models.TextField()),
            ],
        ),
    ]
