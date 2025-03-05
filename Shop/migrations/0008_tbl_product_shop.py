# Generated by Django 5.1.3 on 2025-03-05 11:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0014_delete_tbl_work'),
        ('Shop', '0007_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_product',
            name='shop',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_shop'),
            preserve_default=False,
        ),
    ]
