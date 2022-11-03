# Generated by Django 3.2.13 on 2022-11-03 02:29

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HotPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotplace', models.CharField(max_length=100)),
                ('addr', models.CharField(max_length=80)),
                ('x', models.CharField(max_length=80)),
                ('y', models.CharField(max_length=80)),
                ('theme', models.CharField(max_length=80)),
                ('country', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('content', models.TextField()),
                ('grade', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hotplace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.hotplace')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ImageReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('reviews', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.reviews')),
            ],
        ),
        migrations.CreateModel(
            name='ImageLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.location')),
            ],
        ),
        migrations.CreateModel(
            name='ImageHotPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('hotplace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.hotplace')),
            ],
        ),
        migrations.AddField(
            model_name='hotplace',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.location'),
        ),
    ]
