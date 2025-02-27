# Generated by Django 5.1.3 on 2025-02-13 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Designer', '0003_delete_tbl_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designer_id', models.CharField(max_length=50)),
                ('gallery_photo', models.FileField(upload_to='Assets/designer/photo/')),
            ],
        ),
    ]
