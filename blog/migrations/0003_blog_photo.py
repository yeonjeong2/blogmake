# Generated by Django 4.0.4 on 2022-07-05 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_content_blog_content_rename_title_blog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='blog_photo'),
        ),
    ]