# Generated by Django 3.2.9 on 2021-11-27 00:20

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("triage", "0002_auto_20211126_0713"),
    ]

    operations = [
        migrations.AlterField(
            model_name="case",
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
                default="N",
                max_length=2,
            ),
        ),
        migrations.CreateModel(
            name="ToolDefect",
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
                (
                    "uuid",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
                ),
                ("title", models.CharField(max_length=1024)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("N", "New"),
                            ("A", "Active"),
                            ("R", "Resolved"),
                            ("D", "Deleted"),
                            ("CL", "Closed"),
                            ("NS", "Not Specified"),
                        ],
                        default="N",
                        max_length=2,
                    ),
                ),
                ("finding", models.ManyToManyField(to="triage.Finding")),
                ("notes", models.ManyToManyField(to="triage.Note")),
                (
                    "tool",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="triage.tool"
                    ),
                ),
            ],
        ),
    ]
