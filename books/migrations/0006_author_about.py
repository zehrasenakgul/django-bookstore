# Generated by Django 4.0.3 on 2022-03-28 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_book_image_alter_author_created_alter_author_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='about',
            field=models.CharField(default=1, max_length=500, verbose_name='Yazar Hakkında'),
            preserve_default=False,
        ),
    ]
