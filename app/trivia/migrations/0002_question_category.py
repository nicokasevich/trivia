# Generated by Django 4.0.4 on 2022-04-27 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('sports', 'Sports'), ('history', 'History'), ('music', 'Music')], default=0, max_length=25),
            preserve_default=False,
        ),
    ]