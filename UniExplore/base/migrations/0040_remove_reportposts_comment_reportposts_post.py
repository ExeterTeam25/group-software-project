# Generated by Django 4.0.2 on 2022-03-23 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0039_alter_profile_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportposts',
            name='comment',
        ),
        migrations.AddField(
            model_name='reportposts',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.responses'),
            preserve_default=False,
        ),
    ]
