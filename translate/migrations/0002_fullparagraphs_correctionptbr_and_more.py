# Generated by Django 4.0 on 2022-06-26 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fullparagraphs',
            name='correctionPtBR',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='fullparagraphs',
            name='correctionPtUS',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='phrases',
            name='correctionPtBR',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='phrases',
            name='correctionPtUS',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='words',
            name='correctionPtBR',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='words',
            name='correctionPtUS',
            field=models.TextField(default=''),
        ),
    ]