# Generated by Django 2.2.7 on 2019-12-03 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_puzzle_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puzzle',
            name='account',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]