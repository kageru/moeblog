# Generated by Django 2.0b1 on 2017-11-16 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_article_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='htmlname',
            field=models.CharField(default='adaptivegrain', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
