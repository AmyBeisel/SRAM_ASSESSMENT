# Generated by Django 3.1.7 on 2021-03-22 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikeparts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrontWheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.TextField(max_length=200)),
                ('size', models.TextField(max_length=10)),
                ('weight', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RearWheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.TextField(max_length=200)),
                ('size', models.TextField(max_length=10)),
                ('weight', models.IntegerField()),
            ],
        ),
    ]
