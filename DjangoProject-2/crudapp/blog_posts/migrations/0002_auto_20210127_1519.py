# Generated by Django 3.1.5 on 2021-01-27 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='table',
            name='Date_of_Delivery',
        ),
        migrations.RemoveField(
            model_name='table',
            name='T_size',
        ),
        migrations.RemoveField(
            model_name='table',
            name='T_width',
        ),
    ]
