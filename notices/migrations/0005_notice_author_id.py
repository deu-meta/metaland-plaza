# Generated by Django 4.0.3 on 2022-06-07 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notices", "0004_alter_notice_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="notice",
            name="author_id",
            field=models.CharField(default="00000000-0000-0000-0000-000000000000", editable=False, max_length=36),
            preserve_default=False,
        ),
    ]