# Generated by Django 2.0b1 on 2017-11-15 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('autor', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article')),
            ],
        ),
    ]