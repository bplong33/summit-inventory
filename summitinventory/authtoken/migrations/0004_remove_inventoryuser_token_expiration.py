# Generated by Django 4.0.5 on 2022-07-02 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0003_alter_inventoryuser_token_expiration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventoryuser',
            name='token_expiration',
        ),
    ]
