# Generated by Django 2.2.1 on 2019-06-11 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20190611_0852'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Category_description',
            new_name='category_description',
        ),
        migrations.AlterField(
            model_name='category',
            name='category_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='complaint_id',
            field=models.AutoField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='subcategory_id',
            field=models.AutoField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
