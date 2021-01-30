# Generated by Django 3.1.5 on 2021-01-27 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('T_size', models.IntegerField()),
                ('T_width', models.IntegerField()),
                ('Date_of_Delivery', models.DateField()),
                ('Quantity', models.IntegerField()),
                ('Address', models.CharField(max_length=70)),
            ],
        ),
    ]