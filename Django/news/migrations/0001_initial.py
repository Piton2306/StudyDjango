# Generated by Django 3.1.7 on 2021-07-20 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('anons', models.CharField(max_length=250, verbose_name='Анонс')),
                ('ful_text', models.TextField(verbose_name='Статья')),
                ('data', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]