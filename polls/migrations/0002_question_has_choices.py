# Generated by Django 3.0.8 on 2020-08-15 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='has_choices',
            field=models.BooleanField(default=False, verbose_name='Has choices'),
            preserve_default=False,
        ),
    ]