# Generated by Django 4.2.11 on 2024-04-30 13:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True, null=True, upload_to="avatars/", verbose_name="Аватар"
            ),
        ),
    ]