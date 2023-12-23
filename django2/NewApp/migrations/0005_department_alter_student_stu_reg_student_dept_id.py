# Generated by Django 5.0 on 2023-12-23 09:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("NewApp", "0004_rename_stu_id_student_stu_reg"),
    ]

    operations = [
        migrations.CreateModel(
            name="Department",
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
                ("dept_name", models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name="student",
            name="stu_reg",
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name="student",
            name="dept_id",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.PROTECT,
                to="NewApp.department",
            ),
        ),
    ]