# Generated by Django 2.0b1 on 2017-11-16 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20171116_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='htmlname',
            field=models.CharField(max_length=255),
        ),
    ]