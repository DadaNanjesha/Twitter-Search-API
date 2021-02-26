# Generated by Django 3.1.7 on 2021-02-26 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitterdata',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='twitterdata',
            name='favorite_count',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='twitterdata',
            name='retweet_count',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='twitterdata',
            name='url',
            field=models.URLField(default='www.google.com'),
        ),
        migrations.AlterField(
            model_name='twitterdata',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
