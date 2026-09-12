from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('keepAccount', '0016_alter_assets_user'),
    ]

    operations = [
        # Update display labels only; preserve all existing stored category values.
        migrations.AlterField(
            model_name='account',
            name='type',
            field=models.CharField(
                choices=[
                    ('食', 'Food'),
                    ('衣', 'Clothing'),
                    ('住', 'Housing'),
                    ('行', 'Transportation'),
                    ('育', 'Education'),
                    ('樂', 'Entertainment'),
                    ('收入', 'Income'),
                    ('其他', 'Other'),
                ],
                default='1',
                max_length=20,
            ),
        ),
    ]
