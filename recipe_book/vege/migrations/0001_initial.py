# Generated by Django 4.2.2 on 2023-06-23 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Recipes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("recipe_name", models.CharField(max_length=100)),
                ("recipe_desc", models.TextField()),
                ("recipe_image", models.ImageField(upload_to="recipe_images")),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-updated"],
            },
        ),
    ]