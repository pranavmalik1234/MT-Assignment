# Generated by Django 3.0.8 on 2020-07-06 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaders', '0002_levels_tests_user_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tests',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
