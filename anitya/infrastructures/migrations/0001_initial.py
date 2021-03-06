# Generated by Django 2.1.7 on 2019-04-11 07:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('plugin', models.CharField(default='', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Physical',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('category', models.CharField(default='UNKNOWN', max_length=200)),
                ('driver_id', models.CharField(default='', max_length=36)),
                ('ip_address', models.CharField(default='', max_length=15)),
                ('secret_key', models.CharField(default='', max_length=50)),
                ('az', models.CharField(default='', max_length=50)),
                ('description', models.CharField(default='', max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Virtual',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('physical_id', models.CharField(default='UNKNOWN', max_length=36)),
                ('tags', models.CharField(default='UNKNOWN', max_length=200)),
                ('description', models.CharField(default='', max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
