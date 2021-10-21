# Generated by Django 3.2 on 2021-10-20 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20211020_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='extraimage1',
            field=models.ImageField(blank=True, null=True, upload_to='products/%Y/%m'),
        ),
        migrations.AddField(
            model_name='product',
            name='extraimage2',
            field=models.ImageField(blank=True, null=True, upload_to='products/%Y/%m'),
        ),
        migrations.AddField(
            model_name='product',
            name='extraimage3',
            field=models.ImageField(blank=True, null=True, upload_to='products/%Y/%m'),
        ),
        migrations.AddField(
            model_name='product',
            name='sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
