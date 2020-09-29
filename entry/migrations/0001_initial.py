# Generated by Django 2.2.10 on 2020-02-26 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=100, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ['slug'],
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('text', models.TextField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_edit', models.DateTimeField(auto_now=True)),
                ('tags', models.ManyToManyField(blank=True, to='entry.Tag')),
            ],
            options={
                'verbose_name_plural': 'entries',
                'ordering': ['slug'],
            },
        ),
    ]
