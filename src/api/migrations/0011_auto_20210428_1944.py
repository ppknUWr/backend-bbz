# Generated by Django 3.2 on 2021-04-28 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_templatemodel_to_tb_test_2018'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TemplateModel_To_Tb_Test_2018',
            new_name='TemplateModel_To_Tb_Bibligoraphy_1',
        ),
        migrations.AlterModelTable(
            name='templatemodel_to_tb_bibligoraphy_1',
            table='tb_bibligoraphy_1',
        ),
    ]
