# Generated by Django 3.0.4 on 2020-03-25 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200324_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='portfolio/images/avatar.jpg', upload_to='portfolio/images'),
        ),
    ]