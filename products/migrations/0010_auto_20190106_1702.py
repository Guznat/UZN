# Generated by Django 2.1.4 on 2019-01-06 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20190106_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='extra_info',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
