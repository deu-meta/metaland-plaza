# Generated by Django 4.0.3 on 2022-05-18 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('QA', 'Q&A게시판'), ('F', '자유게시판')], max_length=2),
        ),
    ]
