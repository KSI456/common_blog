# Generated by Django 3.2 on 2021-07-10 07:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_comment_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]