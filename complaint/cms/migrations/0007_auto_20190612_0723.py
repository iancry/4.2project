# Generated by Django 2.2.1 on 2019-06-12 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_auto_20190612_0718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('reg_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='complaints',
            name='complainant_id',
        ),
        migrations.DeleteModel(
            name='Complainants',
        ),
        migrations.AddField(
            model_name='complaints',
            name='user_id',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='cms.Users'),
            preserve_default=False,
        ),
    ]
