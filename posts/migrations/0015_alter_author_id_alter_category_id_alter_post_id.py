# Generated by Django 4.1.7 on 2023-03-18 00:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0014_auto_20230317_0859"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]