# Generated by Django 3.2.25 on 2024-03-14 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
