# Generated by Django 5.1.1 on 2024-10-06 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quickcommerce", "0008_order_email_order_full_name_order_phone_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="store",
            name="owner_email",
            field=models.CharField(default="chinmaychopade23@gmail.com", max_length=100),
            preserve_default=False,
        ),
    ]