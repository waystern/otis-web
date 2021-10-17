# Generated by Django 3.2.8 on 2021-10-17 22:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0061_alter_problemsuggestion_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problemsuggestion',
            name='student',
        ),
        migrations.AlterField(
            model_name='problemsuggestion',
            name='user',
            field=models.ForeignKey(help_text='User who suggested the problem.', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
