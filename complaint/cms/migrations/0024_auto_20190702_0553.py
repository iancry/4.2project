# Generated by Django 2.2.1 on 2019-07-02 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0023_auto_20190625_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_name', models.CharField(max_length=50)),
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='complainants',
            name='complainant_contact',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='subcategory_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='category',
            name='department_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cms.Department'),
        ),
    ]