# Generated by Django 4.2.5 on 2023-10-08 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("appCoder", "0006_user_first_name_user_username"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="User",
            new_name="User_mio",
        ),
    ]
