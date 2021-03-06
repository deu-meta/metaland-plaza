# Generated by Django 4.0.3 on 2022-05-18 20:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0002_alter_notice_notion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notice',
            options={'ordering': ['-id'], 'verbose_name': '공지사항', 'verbose_name_plural': '공지사항'},
        ),
        migrations.AddField(
            model_name='notice',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
