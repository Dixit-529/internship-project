# Generated by Django 3.0 on 2022-07-10 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Electronics', '0005_auto_20220709_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('username', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('MobileNo', models.PositiveIntegerField()),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]