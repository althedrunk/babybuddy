# Generated migration for weight_unit setting
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("babybuddy", "0035_alter_settings_language"),
    ]

    operations = [
        migrations.AddField(
            model_name="settings",
            name="weight_unit",
            field=models.CharField(
                choices=[
                    ("kg", "Kilograms (kg)"),
                    ("lb", "Pounds and ounces (lbs/oz)"),
                ],
                default="lb",
                max_length=8,
                verbose_name="Weight Unit",
            ),
        ),
    ]
