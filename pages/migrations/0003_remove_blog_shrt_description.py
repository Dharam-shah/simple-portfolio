# Generated by Django 4.0.4 on 2022-04-15 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='shrt_description',
        ),
    ]