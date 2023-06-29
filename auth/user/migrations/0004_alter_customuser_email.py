# Generated by Django 4.2.2 on 2023-06-29 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_customuser_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="email address"
            ),
        ),
    ]
