# Generated by Django 2.2.16 on 2022-03-01 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20220301_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/', verbose_name='Картинка'),
        ),
    ]
