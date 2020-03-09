# Generated by Django 3.0.4 on 2020-03-07 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapbookTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(upload_to='images')),
                ('title', models.CharField(max_length=50)),
                ('experience', models.CharField(max_length=5000)),
            ],
        ),
    ]
