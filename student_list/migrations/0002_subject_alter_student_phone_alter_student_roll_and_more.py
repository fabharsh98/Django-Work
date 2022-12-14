# Generated by Django 4.1.3 on 2022-11-30 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("student_list", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subject",
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
                ("title", models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name="student", name="phone", field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="student", name="roll", field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="student",
            name="subject",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="student_list.subject"
            ),
        ),
    ]
