# Generated by Django 5.1.7 on 2025-03-24 07:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("citizens", "0027_alter_crimereport_evidence_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="crimereport",
            name="tracking_number",
            field=models.CharField(
                default="ea5fe9e771", editable=False, max_length=20, unique=True
            ),
        ),
    ]
