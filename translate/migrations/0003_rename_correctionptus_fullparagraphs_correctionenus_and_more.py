# Generated by Django 4.0 on 2022-06-26 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translate', '0002_fullparagraphs_correctionptbr_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fullparagraphs',
            old_name='correctionPtUS',
            new_name='correctionEnUS',
        ),
        migrations.RenameField(
            model_name='phrases',
            old_name='correctionPtUS',
            new_name='correctionEnUS',
        ),
        migrations.RenameField(
            model_name='words',
            old_name='correctionPtUS',
            new_name='correctionEnUS',
        ),
    ]
