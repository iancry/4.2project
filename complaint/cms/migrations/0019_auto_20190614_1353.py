# Generated by Django 2.2.1 on 2019-06-14 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0018_auto_20190614_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='remark',
            field=models.CharField(max_length=700),
        ),
        migrations.CreateModel(
            name='ComplaintRemark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.CharField(max_length=700)),
                ('remark_date', models.DateTimeField(auto_now=True)),
                ('complaint_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Complaints')),
            ],
        ),
    ]
