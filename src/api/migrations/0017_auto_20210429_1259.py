# Generated by Django 3.2 on 2021-04-29 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_delete_table_bibliography_1'),
    ]

    operations = [
        migrations.CreateModel(
            name='bibliography_db_1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'bibliography_db_1',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='bibliography_db_2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'bibliography_db_2',
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='bibliography_test',
        ),
        migrations.DeleteModel(
            name='bibliography_test_1',
        ),
    ]
