# Generated by Django 3.0.4 on 2020-03-25 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200324_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='blog/images/avatar.jpg', upload_to='blog/images'),
        ),
    ]
