# Generated by Django 4.0.1 on 2022-03-15 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_merge_20220315_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weeklychallenge',
            name='renewed',
        ),
        migrations.AddField(
            model_name='challenges',
            name='is_weekly_challenge',
            field=models.BooleanField(default=False),
        ),
    ]
