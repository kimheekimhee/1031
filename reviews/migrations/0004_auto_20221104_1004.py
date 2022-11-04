# Generated by Django 3.2.13 on 2022-11-04 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20221103_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='country',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='hotplace',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotplace', to='reviews.location'),
        ),
    ]