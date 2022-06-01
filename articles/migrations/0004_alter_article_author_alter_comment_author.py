# Generated by Django 4.0.3 on 2022-05-25 21:25

from django.db import migrations
import metaland.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_options_alter_comment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=metaland.models.TokenUserField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=metaland.models.TokenUserField(),
        ),
    ]