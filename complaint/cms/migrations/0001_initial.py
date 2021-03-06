# Generated by Django 2.2.1 on 2019-06-10 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('admin_username', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=200)),
                ('Category_description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('reg_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('subcategory_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('subcategory_name', models.CharField(max_length=100)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('complaint_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Category')),
                ('subcategory_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Subcategory')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Users')),
            ],
        ),
        migrations.CreateModel(
            name='ComplaintRemark',
            fields=[
                ('remark_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=100)),
                ('remark', models.CharField(max_length=700)),
                ('remark_date', models.DateTimeField(auto_now=True)),
                ('complaint_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Complaints')),
            ],
        ),
        migrations.CreateModel(
            name='ComplaintDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_type', models.CharField(max_length=100)),
                ('complaint_details', models.CharField(max_length=1000)),
                ('complaint_file', models.FileField(upload_to='files/')),
                ('status', models.CharField(max_length=100)),
                ('reg_date', models.DateTimeField(auto_now=True)),
                ('complaint_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Complaints')),
            ],
        ),
    ]
