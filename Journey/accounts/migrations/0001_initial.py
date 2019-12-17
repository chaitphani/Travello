# Generated by Django 2.2.1 on 2019-09-04 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=30, null=True)),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('mob', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=8)),
                ('image', models.ImageField(max_length=10, upload_to='')),
            ],
        ),
    ]
