# Generated by Django 2.0.4 on 2018-04-26 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='levelquestion',
            name='feedback',
            field=models.TextField(blank=True),
        ),
    ]
