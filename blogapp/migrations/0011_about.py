# Generated by Django 3.0.6 on 2020-08-21 18:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0010_auto_20200813_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
