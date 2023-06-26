# Generated by Django 4.2.2 on 2023-06-25 22:03

from django.db import migrations, models
import example.models


class Migration(migrations.Migration):

    dependencies = [
        ("example", "0003_remove_image_folder_name_remove_image_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="name",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="image",
            name="file",
            field=models.ImageField(upload_to=example.models.Image.nameFile),
        ),
    ]
