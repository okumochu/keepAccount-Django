# Generated by Django 4.1.3 on 2022-12-26 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keepAccount', '0010_alter_account_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date',
            field=models.DateField(verbose_name='2022-12-26'),
        ),
    ]
