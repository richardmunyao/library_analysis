# Generated by Django 4.0.2 on 2022-03-14 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0004_alter_document_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='subjects',
            field=models.TextField(default='Fiction'),
            preserve_default=False,
        ),
    ]
