# Generated by Django 4.1.3 on 2022-12-24 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keepAccount', '0004_remove_account_username_account_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='money',
            new_name='cost',
        ),
        migrations.AlterField(
            model_name='account',
            name='type',
            field=models.CharField(choices=[('1', '食'), ('2', '衣'), ('3', '住'), ('4', '行'), ('5', '育'), ('6', '樂'), ('7', '其他')], default='1', max_length=20),
        ),
    ]
