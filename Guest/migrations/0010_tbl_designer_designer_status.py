# Generated by Django 5.1.3 on 2025-02-11 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0009_tbl_shop_shop_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_designer',
            name='designer_status',
            field=models.IntegerField(default=0),
        ),
    ]
