"""
Convert Weight.weight values from the legacy "lbs.oz" float format
(e.g. 13.7 meaning 13 lbs 7 oz) to total ounces (e.g. 215).

The old format stored the oz digits after the decimal point, so:
  13.7  -> 13 lbs  7 oz -> 215 oz
  9.14  ->  9 lbs 14 oz -> 158 oz
  8.0   ->  8 lbs  0 oz -> 128 oz

Note: floats like 9.10 were stored as 9.1 by Python, so any entry
that was originally 9 lbs 10 oz cannot be distinguished from
9 lbs 1 oz. Those edge cases are migrated as 1 oz.
"""
from django.db import migrations


def lbs_oz_float_to_total_oz(apps, schema_editor):
    Weight = apps.get_model("core", "Weight")
    for w in Weight.objects.all():
        if w.weight is None:
            continue
        val_str = str(round(w.weight, 10))
        if "." in val_str:
            lbs = int(val_str.split(".")[0])
            oz = int(val_str.split(".")[1])
        else:
            lbs = int(float(val_str))
            oz = 0
        w.weight = lbs * 16 + oz
        w.save(update_fields=["weight"])


def total_oz_to_lbs_oz_float(apps, schema_editor):
    """Reverse: convert total oz back to lbs.oz float (best-effort)."""
    Weight = apps.get_model("core", "Weight")
    for w in Weight.objects.all():
        if w.weight is None:
            continue
        total_oz = int(round(w.weight))
        lbs = total_oz // 16
        oz = total_oz % 16
        w.weight = float(f"{lbs}.{oz}")
        w.save(update_fields=["weight"])


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0035_recalculate_durations"),
    ]

    operations = [
        migrations.RunPython(
            lbs_oz_float_to_total_oz,
            reverse_code=total_oz_to_lbs_oz_float,
        ),
    ]
