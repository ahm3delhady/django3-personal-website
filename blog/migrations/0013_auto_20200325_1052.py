# Generated by Django 3.0.4 on 2020-03-25 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200324_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='static/img/avatar/avatar.jpg', upload_to='blog/images'),
        ),
    ]