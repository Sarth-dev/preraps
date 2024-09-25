# Generated by Django 5.1.1 on 2024-09-22 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quickcommerce", "0005_category_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="brand",
            name="slug",
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]