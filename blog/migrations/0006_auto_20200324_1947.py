# Generated by Django 3.0.4 on 2020-03-25 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='static/blog/images/avatar.jpg', upload_to='blog/images'),
        ),
    ]
