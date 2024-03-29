# Generated by Django 3.2.6 on 2021-08-23 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_metadbinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='augustyn_corpus1_the_global_book_publishing_market',
            name='author',
        ),
        migrations.RemoveField(
            model_name='augustyn_global_book_publishing_2001_2018',
            name='author',
        ),
        migrations.RemoveField(
            model_name='bernacki_miedzywojenna_fantastyka',
            name='author',
        ),
        migrations.RemoveField(
            model_name='cislo_irlandia',
            name='author',
        ),
        migrations.RemoveField(
            model_name='hojka_slowniki_dla_dzieci_1989_2015',
            name='author',
        ),
        migrations.RemoveField(
            model_name='lubocki_bibliografia_elementarzy_1945_2012_podmiotowa',
            name='author',
        ),
        migrations.RemoveField(
            model_name='lubocki_bibliografia_elementarzy_1945_2012_przedmiotowa',
            name='author',
        ),
        migrations.RemoveField(
            model_name='lubocki_bibliografia_podmiotowa_stefanii_grodzienskiej',
            name='author',
        ),
        migrations.RemoveField(
            model_name='lubocki_bibliografia_przedmiotowa_stefanii_grodzienskiej',
            name='author',
        ),
        migrations.RemoveField(
            model_name='nabialczyk_bibliografia_o_iinib_uwr',
            name='author',
        ),
        migrations.AlterField(
            model_name='metadbinfo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
