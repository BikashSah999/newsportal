# Generated by Django 3.0.6 on 2020-08-21 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0015_auto_20200822_0055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='about',
            new_name='about_title',
        ),
    ]
