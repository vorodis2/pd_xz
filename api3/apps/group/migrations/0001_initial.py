# Generated by Django 3.1.4 on 2021-08-19 07:17

import api.utils
import apps.group.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('up', models.BooleanField(default=False, verbose_name='апрув up')),
                ('public', models.BooleanField(default=False, verbose_name='публичны public')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Имя name')),
                ('json', models.JSONField(blank=True, null=True, verbose_name='JSON json')),
                ('icon', models.CharField(default='favicon.ico', max_length=512, verbose_name='Иконка icon')),
                ('iconId', models.PositiveIntegerField(default=0, verbose_name='ид Файла iconId')),
                ('ru', models.CharField(blank=True, default='programText(Вставка)', max_length=255, verbose_name='текст ru')),
                ('en', models.CharField(blank=True, default='programText(Вставка)', max_length=255, verbose_name='text en')),
            ],
            options={
                'verbose_name': 'Объект',
                'verbose_name_plural': 'Объекты',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupSort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Не установлено', max_length=255, verbose_name='Сортировка')),
            ],
            options={
                'verbose_name': 'Сортировка',
                'verbose_name_plural': 'Сортировки',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.FileField(upload_to=api.utils.create_file_upload_path, verbose_name='Файл')),
                ('rel_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='group.group')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Не установлено', max_length=255, verbose_name='title')),
                ('text', models.TextField(blank=True, max_length=1255, verbose_name='комент')),
                ('comment_obj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='group.group', verbose_name='koment')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='автор')),
            ],
            options={
                'verbose_name': 'комент',
                'verbose_name_plural': 'коменты',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='group',
            name='sort',
            field=models.ForeignKey(default=apps.group.models.get_default_sort, on_delete=django.db.models.deletion.SET_DEFAULT, to='group.groupsort', verbose_name='Сортировка sort'),
        ),
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Юзер user'),
        ),
    ]
