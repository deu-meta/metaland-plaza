# Generated by Django 4.0.3 on 2022-05-11 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Space',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('B', '건물'), ('D', '학과'), ('F', '동아리')], max_length=3)),
                ('thumbnail', models.ImageField(default='default_image.jpg', upload_to='')),
                ('short_introduce', models.CharField(default='소개없음', max_length=200)),
                ('long_introduce', models.TextField(default='글 없음')),
            ],
            options={
                'verbose_name': '공간',
                'verbose_name_plural': '공간',
            },
        ),
    ]
