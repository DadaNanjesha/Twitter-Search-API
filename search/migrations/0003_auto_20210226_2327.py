# Generated by Django 3.1.7 on 2021-02-26 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20210226_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitterdata',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
