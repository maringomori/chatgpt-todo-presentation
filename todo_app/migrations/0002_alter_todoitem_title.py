# Generated by Django 4.2 on 2023-04-21 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todoitem",
            name="title",
            field=models.CharField(max_length=500),
        ),
    ]
