# Generated by Django 4.0.4 on 2022-07-05 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commenet',
            new_name='comment',
        ),
    ]