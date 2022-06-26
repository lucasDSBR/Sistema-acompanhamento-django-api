# Generated by Django 4.0 on 2022-06-26 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FullParagraphs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptBR', models.TextField(default='')),
                ('enUS', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Phrases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptBR', models.TextField(default='')),
                ('enUS', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptBR', models.TextField(default='')),
                ('enUS', models.TextField(default='')),
            ],
        ),
    ]
