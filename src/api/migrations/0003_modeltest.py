# Generated by Django 3.2 on 2021-05-21 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210521_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelTest',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('test', models.CharField(max_length=50)),
            ],
        ),
    ]
