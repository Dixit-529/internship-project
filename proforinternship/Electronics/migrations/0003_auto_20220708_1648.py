# Generated by Django 3.0 on 2022-07-08 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Electronics', '0002_auto_20220702_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessories',
            name='catagory',
            field=models.CharField(default='Laptop', max_length=11),
        ),
        migrations.AddField(
            model_name='laptops',
            name='catagory',
            field=models.CharField(default='Accessories', max_length=11),
        ),
        migrations.AddField(
            model_name='mobiles',
            name='catagory',
            field=models.CharField(default='Mobile', max_length=11),
        ),
    ]