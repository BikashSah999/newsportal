# Generated by Django 3.0.6 on 2020-08-21 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0014_auto_20200822_0054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='category',
            new_name='categorylist',
        ),
    ]