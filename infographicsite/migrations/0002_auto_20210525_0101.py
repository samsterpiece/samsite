# Generated by Django 3.2.3 on 2021-05-25 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infographicsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilesUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
