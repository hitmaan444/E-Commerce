# Generated by Django 5.0.4 on 2024-05-29 12:55

import shortuuid.django_fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="cid",
            field=shortuuid.django_fields.ShortUUIDField(
                alphabet="abcdefghijklm12345",
                length=22,
                max_length=30,
                prefix="cat",
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="pid",
            field=shortuuid.django_fields.ShortUUIDField(
                alphabet="abclm12345", length=22, max_length=30, prefix="", unique=True
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="sku",
            field=shortuuid.django_fields.ShortUUIDField(
                alphabet="1234567890",
                length=22,
                max_length=40,
                prefix="sku",
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="vendor",
            name="vid",
            field=shortuuid.django_fields.ShortUUIDField(
                alphabet="abcdefghijklm12345",
                length=22,
                max_length=30,
                prefix="ven",
                unique=True,
            ),
        ),
    ]
