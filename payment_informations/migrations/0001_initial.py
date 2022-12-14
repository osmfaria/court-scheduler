# Generated by Django 4.1.1 on 2022-09-13 16:57

import creditcards.models
from django.db import migrations, models
import django_cryptography.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PaymentInformation",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "number",
                    django_cryptography.fields.encrypt(
                        creditcards.models.CardNumberField(
                            max_length=25, verbose_name="card number"
                        )
                    ),
                ),
                (
                    "code",
                    django_cryptography.fields.encrypt(
                        creditcards.models.SecurityCodeField(
                            max_length=4, verbose_name="security code"
                        )
                    ),
                ),
                (
                    "expiration_date",
                    django_cryptography.fields.encrypt(
                        models.CharField(max_length=250)
                    ),
                ),
            ],
        ),
    ]
