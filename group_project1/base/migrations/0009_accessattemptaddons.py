# Generated by Django 4.0.2 on 2022-02-25 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('axes', '0007_alter_accessattempt_unique_together'),
        ('base', '0008_challenges_lat_challenges_long'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessAttemptAddons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration_date', models.DateTimeField(verbose_name='Expiration Time')),
                ('accessattempt', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='axes.accessattempt')),
            ],
        ),
    ]
