# Generated by Django 2.2.1 on 2019-05-12 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmazonSearch', '0005_auto_20190511_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='page',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='search',
            name='pages',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='search',
            name='position',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='search',
            name='sales_rank',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='title',
            name='batch',
            field=models.CharField(max_length=16),
        ),
    ]
