# Generated by Django 2.1.7 on 2019-02-27 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-update_time', '-id']},
        ),
    ]