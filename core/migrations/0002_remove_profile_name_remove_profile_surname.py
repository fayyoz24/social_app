# Generated by Django 4.1 on 2022-09-02 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="profile", name="name",),
        migrations.RemoveField(model_name="profile", name="surname",),
    ]
