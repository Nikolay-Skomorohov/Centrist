# Generated by Django 3.1.4 on 2020-12-16 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newsletters", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscriberslist",
            name="subscriber_email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
