# Generated by Django 3.0.3 on 2020-03-01 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intellect', '0002_auto_20200301_0821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_discription',
        ),
        migrations.AddField(
            model_name='post',
            name='post_description',
            field=models.TextField(default='This area write image description'),
        ),
    ]
