# Generated by Django 3.2.6 on 2021-08-15 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_augustyn_corpus1_the_global_book_publishing_market_augustyn_global_book_publishing_2001_2018_bernack'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaDBInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_name', models.CharField(max_length=200)),
                ('real_db_name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]
