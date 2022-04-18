# Generated by Django 2.2.16 on 2022-03-11 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20220308_1227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='follow',
            options={'verbose_name_plural': 'Подписки'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name_plural': 'Группы'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.Post', verbose_name='Коментарии'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL, verbose_name='Подписчик'),
        ),
    ]
