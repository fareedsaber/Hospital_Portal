# Generated by Django 3.1.5 on 2021-05-21 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0002_remove_sec_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sec',
            name='Dep',
        ),
        migrations.AddField(
            model_name='dep',
            name='secN',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='acc.sec'),
            preserve_default=False,
        ),
    ]