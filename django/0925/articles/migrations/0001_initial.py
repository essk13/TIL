# Generated by Django 3.2.6 on 2021-09-26 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('context', models.TextField()),
                ('img', models.ImageField(blank=True, upload_to='%Y/%m/%d')),
            ],
        ),
    ]
