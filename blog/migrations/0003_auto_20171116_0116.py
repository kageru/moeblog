# Generated by Django 2.0b1 on 2017-11-16 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171116_0022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='post_id',
            new_name='article_id',
        ),
    ]
