# Generated by Django 5.1.1 on 2024-09-27 16:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_alter_corner_options_alter_feedback_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="measurement",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
