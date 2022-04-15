# Generated by Django 4.0.4 on 2022-04-15 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=250)),
                ('shrt_description', models.TextField()),
                ('blog_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
        ),
    ]