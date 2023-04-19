# Generated by Django 4.0 on 2021-12-24 16:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("triage", "0014_remove_finding_scan_finding_normalized_title_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="finding",
            name="analyst_severity_level",
            field=models.CharField(
                choices=[
                    ("NS", "Not Specified"),
                    ("NO", "None"),
                    ("IN", "Informational"),
                    ("VL", "Very Low"),
                    ("L", "Low"),
                    ("M", "Medium"),
                    ("H", "High"),
                    ("VH", "Very High"),
                ],
                db_index=True,
                default="NS",
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="finding",
            name="normalized_title",
            field=models.CharField(
                blank=True, db_index=True, max_length=1024, null=True
            ),
        ),
        migrations.AlterField(
            model_name="finding",
            name="severity_level",
            field=models.CharField(
                choices=[
                    ("NS", "Not Specified"),
                    ("NO", "None"),
                    ("IN", "Informational"),
                    ("VL", "Very Low"),
                    ("L", "Low"),
                    ("M", "Medium"),
                    ("H", "High"),
                    ("VH", "Very High"),
                ],
                db_index=True,
                default="NS",
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="finding",
            name="state",
            field=models.CharField(
                choices=[
                    ("N", "New"),
                    ("A", "Active"),
                    ("R", "Resolved"),
                    ("D", "Deleted"),
                    ("CL", "Closed"),
                    ("NS", "Not Specified"),
                ],
                db_index=True,
                default="N",
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="finding",
            name="title",
            field=models.CharField(db_index=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name="projectversion",
            name="files",
            field=models.ManyToManyField(blank=True, to="triage.File"),
        ),
    ]
