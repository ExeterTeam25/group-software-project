# Generated by Django 4.0.1 on 2022-02-25 16:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ('base', '0009_alter_responses_challenge'),
    ]

    operations = [
        migrations.AddField(
            model_name='responses',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
