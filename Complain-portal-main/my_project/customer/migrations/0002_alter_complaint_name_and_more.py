# Generated by Django 5.0.1 on 2024-01-17 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='product_category',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='product_name',
            field=models.TextField(),
        ),
    ]
