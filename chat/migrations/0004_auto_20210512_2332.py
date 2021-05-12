# Generated by Django 3.2.1 on 2021-05-12 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20210512_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyBanner',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('cover', models.ImageField(upload_to='images/', verbose_name='Изображение')),
            ],
        ),
        migrations.DeleteModel(
            name='Banner',
        ),
    ]