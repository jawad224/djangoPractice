# Generated by Django 4.1.3 on 2022-12-23 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=122)),
                ('phpne', models.CharField(max_length=122)),
                ('desc', models.TextField(max_length=122)),
                ('date', models.DateField()),
            ],
        ),
    ]
