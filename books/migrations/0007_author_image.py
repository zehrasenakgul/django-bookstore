# Generated by Django 4.0.3 on 2022-03-28 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_author_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.CharField(max_length=150, null=True, verbose_name='Yazar Fotoğrafı'),
        ),
    ]
