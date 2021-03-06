# Generated by Django 4.0.1 on 2022-02-27 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0014_merge_20220226_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='responses',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10)),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.responses')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
