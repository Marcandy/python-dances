# Generated by Django 2.1.7 on 2019-03-19 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(default='dsjkds goo'),
            preserve_default=False,
        ),
    ]
