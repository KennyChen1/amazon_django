# Generated by Django 2.2.1 on 2019-05-11 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmazonSearch', '0003_search'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='asin',
            field=models.CharField(default='0', max_length=16),
        ),
        migrations.AddField(
            model_name='search',
            name='author',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='search',
            name='date',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='search',
            name='image_link',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='search',
            name='page',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='search',
            name='pages',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='search',
            name='position',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='search',
            name='publication_date',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='search',
            name='publisher',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='search',
            name='sales_rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='search',
            name='title_text',
            field=models.CharField(default='1', max_length=128),
        ),
        migrations.AlterField(
            model_name='title',
            name='asin',
            field=models.CharField(default='0', max_length=16),
        ),
    ]
