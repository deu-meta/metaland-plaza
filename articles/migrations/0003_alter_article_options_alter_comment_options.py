# Generated by Django 4.0.3 on 2022-05-18 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-id'], 'verbose_name': '게시물', 'verbose_name_plural': '게시물 목록'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['id'], 'verbose_name': '댓글', 'verbose_name_plural': '댓글 목록'},
        ),
    ]
