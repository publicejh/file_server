# Generated by Django 2.2.2 on 2019-06-08 23:24

from django.db import migrations, models
import files.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('sig_id', models.IntegerField()),
                ('photo', models.ImageField(upload_to=files.models.user_directory_path)),
            ],
        ),
    ]
