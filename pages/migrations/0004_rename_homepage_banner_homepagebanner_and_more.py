# Generated by Django 4.0.4 on 2022-04-15 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_remove_blog_shrt_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Homepage_banner',
            new_name='HomepageBanner',
        ),
        migrations.RenameField(
            model_name='homepagebanner',
            old_name='Banner_image',
            new_name='banner_image',
        ),
        migrations.RenameField(
            model_name='homepagebanner',
            old_name='Banner_subtitle',
            new_name='banner_subtitle',
        ),
        migrations.RenameField(
            model_name='homepagebanner',
            old_name='Banner_title',
            new_name='banner_title',
        ),
    ]