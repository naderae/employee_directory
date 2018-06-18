# Generated by Django 2.0.2 on 2018-06-18 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('job_title', models.TextField(blank=True, max_length=255)),
                ('experience', models.IntegerField()),
                ('image', models.FileField(upload_to='images/')),
            ],
        ),
    ]