# Generated by Django 4.1.5 on 2023-03-21 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_leetcode_details_leetcode_acc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leetcode_acc',
            name='last_solved',
            field=models.CharField(blank=True, default='Scraping..', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='leetcode_acc',
            name='name',
            field=models.CharField(blank=True, default='Scraping..', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='leetcode_acc',
            name='number_of_questions',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='leetcode_acc',
            name='photo_url',
            field=models.CharField(blank=True, default='Scarping..', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='leetcode_acc',
            name='rank',
            field=models.CharField(blank=True, default='Scraping..', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='leetcode_acc',
            name='username',
            field=models.CharField(default='', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
