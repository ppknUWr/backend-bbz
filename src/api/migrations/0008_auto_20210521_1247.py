# Generated by Django 3.2 on 2021-05-21 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_augustyn_corpus1_the_global_book_publishing_market_augustyn_global_book_publishing_2001_2018_bernack'),
    ]

    operations = [
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
            model_name='lubocki_bibliografia_podmiotowa_stefanii_grodzieńskiej',
            name='author',
        ),
        migrations.RemoveField(
            model_name='lubocki_bibliografia_przedmiotowa_stefanii_grodzieńskiej',
            name='author',
        ),
        migrations.RemoveField(
            model_name='nabialczyk_bibliografia_o_iinib_uwr',
            name='author',
        ),
        migrations.DeleteModel(
            name='augustyn_corpus1_the_global_book_publishing_market',
        ),
        migrations.DeleteModel(
            name='augustyn_global_book_publishing_2001_2018',
        ),
        migrations.DeleteModel(
            name='bernacki_miedzywojenna_fantastyka',
        ),
        migrations.DeleteModel(
            name='cislo_irlandia',
        ),
        migrations.DeleteModel(
            name='hojka_slowniki_dla_dzieci_1989_2015',
        ),
        migrations.DeleteModel(
            name='lubocki_bibliografia_elementarzy_1945_2012_podmiotowa',
        ),
        migrations.DeleteModel(
            name='lubocki_Bibliografia_elementarzy_1945_2012_przedmiotowa',
        ),
        migrations.DeleteModel(
            name='lubocki_bibliografia_podmiotowa_stefanii_grodzieńskiej',
        ),
        migrations.DeleteModel(
            name='lubocki_bibliografia_przedmiotowa_stefanii_grodzieńskiej',
        ),
        migrations.DeleteModel(
            name='nabialczyk_bibliografia_o_iinib_UWr',
        ),
    ]
