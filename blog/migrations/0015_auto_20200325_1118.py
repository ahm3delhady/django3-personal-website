# Generated by Django 3.0.4 on 2020-03-25 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200325_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='url',
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='blog/images/avatar.jpg', upload_to='blog/images'),
        ),
    ]
