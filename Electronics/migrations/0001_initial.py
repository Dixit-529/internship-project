# Generated by Django 3.0 on 2022-07-01 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.PositiveIntegerField()),
                ('Specifications', models.TextField()),
                ('img', models.ImageField(upload_to='pro/accessories')),
                ('review', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Laptops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.PositiveIntegerField()),
                ('Specifications', models.TextField()),
                ('img', models.ImageField(upload_to='pro/laptops')),
                ('review', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mobiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.PositiveIntegerField()),
                ('Specifications', models.TextField()),
                ('img', models.ImageField(upload_to='pro/mobiles')),
                ('review', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('username', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('MobileNo', models.PositiveIntegerField()),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
