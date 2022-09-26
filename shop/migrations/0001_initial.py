# Generated by Django 2.2 on 2022-09-21 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=50)),
                ('productDescription', models.CharField(max_length=400)),
                ('productPrice', models.FloatField()),
                ('publishDate', models.DateField()),
            ],
        ),
    ]