# Generated by Django 4.0.5 on 2022-07-03 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0004_remove_inventoryuser_token_expiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryuser',
            name='token',
            field=models.CharField(default=0, max_length=1000),
        ),
    ]