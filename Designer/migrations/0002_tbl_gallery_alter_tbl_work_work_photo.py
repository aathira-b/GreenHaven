# Generated by Django 5.1.3 on 2025-02-13 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Designer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_photo', models.FileField(upload_to='Assets/designer/photo/')),
            ],
        ),
        migrations.AlterField(
            model_name='tbl_work',
            name='work_photo',
            field=models.FileField(upload_to='Assets/designer/photo/'),
        ),
    ]
