# Generated by Django 4.1.7 on 2023-02-24 04:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("careers", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="certificate",
            name="file",
        ),
        migrations.AddField(
            model_name="certificate",
            name="image",
            field=models.ImageField(
                default=1, upload_to="certificates/", verbose_name="Certificados"
            ),
            preserve_default=False,
        ),
    ]
