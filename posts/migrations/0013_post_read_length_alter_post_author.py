# Generated by Django 4.1.7 on 2023-03-09 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_post_primary_category_alter_post_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='read_length',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.author'),
        ),
    ]
