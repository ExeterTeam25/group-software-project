# Generated by Django 4.0.1 on 2022-02-26 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_merge_20220226_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='responses',
            name='photograph',
            field=models.ImageField(default='images/challenge-completed.png', upload_to='images/'),
        ),
    ]
