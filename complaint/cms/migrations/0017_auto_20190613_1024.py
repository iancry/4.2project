# Generated by Django 2.2.1 on 2019-06-13 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20190612_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='complainants',
            name='complainantReg_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='complainants',
            name='complainant_contact',
            field=models.CharField(default='22222222', max_length=20),
        ),
    ]
