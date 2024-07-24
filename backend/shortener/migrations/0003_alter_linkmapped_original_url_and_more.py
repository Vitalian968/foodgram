# Generated by Django 4.2.11 on 2024-04-29 22:22

from django.db import migrations, models
import shortener.models


class Migration(migrations.Migration):
    dependencies = [
        ("shortener", "0002_alter_linkmapped_url_hash"),
    ]

    operations = [
        migrations.AlterField(
            model_name="linkmapped",
            name="original_url",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="linkmapped",
            name="url_hash",
            field=models.CharField(
                default=shortener.models.generate_hash, max_length=10
            ),
        ),
    ]
