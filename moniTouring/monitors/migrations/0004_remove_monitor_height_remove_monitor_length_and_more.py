# Generated by Django 5.0.4 on 2024-12-11 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitors', '0003_alter_monitor_brightness_alter_monitor_height_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monitor',
            name='height',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='length',
        ),
        migrations.AddField(
            model_name='monitor',
            name='resolution',
            field=models.CharField(default=100, max_length=15),
            preserve_default=False,
        ),
    ]
