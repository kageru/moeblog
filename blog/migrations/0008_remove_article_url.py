# Generated by Django 2.0b1 on 2017-11-16 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_article_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='url',
        ),
    ]