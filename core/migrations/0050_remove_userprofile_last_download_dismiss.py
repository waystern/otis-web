# Generated by Django 4.1.10 on 2023-08-07 01:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0049_userprofile_show_artwork_on_curriculum"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="last_download_dismiss",
        ),
    ]
