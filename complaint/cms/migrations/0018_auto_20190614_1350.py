# Generated by Django 2.2.1 on 2019-06-14 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0017_auto_20190613_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='remark',
            field=models.CharField(default='we got you', max_length=700),
        ),
        migrations.DeleteModel(
            name='ComplaintRemark',
        ),
    ]
