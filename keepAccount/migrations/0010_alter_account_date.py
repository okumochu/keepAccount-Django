# Generated by Django 4.1.3 on 2022-12-26 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keepAccount', '0009_alter_account_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
