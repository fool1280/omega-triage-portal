# Generated by Django 4.0 on 2021-12-25 03:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("triage", "0015_alter_finding_analyst_severity_level_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tooldefect",
            old_name="finding",
            new_name="findings",
        ),
    ]
