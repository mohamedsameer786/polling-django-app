# Generated by Django 3.2 on 2021-04-14 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0005_remove_vote_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
