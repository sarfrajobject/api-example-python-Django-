# Generated by Django 2.0.2 on 2019-10-26 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0002_auto_20191026_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]
