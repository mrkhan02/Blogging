# Generated by Django 3.1.5 on 2021-05-10 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='fodu',
            field=models.CharField(default='0', max_length=255),
        ),
        migrations.AddField(
            model_name='vote',
            name='gaddar',
            field=models.CharField(default='0', max_length=255),
        ),
        migrations.AddField(
            model_name='vote',
            name='gmg',
            field=models.CharField(default='0', max_length=255),
        ),
        migrations.AddField(
            model_name='vote',
            name='nakre',
            field=models.CharField(default='0', max_length=255),
        ),
    ]