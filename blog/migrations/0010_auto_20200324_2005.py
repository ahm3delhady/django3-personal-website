# Generated by Django 3.0.4 on 2020-03-25 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200324_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='/media/blog/images/avatar.jpg', upload_to='blog/images'),
        ),
    ]