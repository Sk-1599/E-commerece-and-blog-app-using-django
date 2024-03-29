# Generated by Django 3.2 on 2021-09-18 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210914_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=5000)),
                ('email', models.CharField(max_length=90)),
                ('address', models.CharField(max_length=111)),
                ('city', models.CharField(max_length=111)),
                ('state', models.CharField(max_length=111)),
                ('zip_mode', models.CharField(max_length=111)),
            ],
        ),
    ]
