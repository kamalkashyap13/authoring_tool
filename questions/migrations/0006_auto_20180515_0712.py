# Generated by Django 2.0.5 on 2018-05-15 07:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0005_levelquestion_question_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='OffWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Level')),
            ],
        ),
        migrations.RemoveField(
            model_name='levelquestion',
            name='date',
        ),
        migrations.AddField(
            model_name='levelquestion',
            name='concept',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='levelquestion',
            name='contact_time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='levelquestion',
            name='difficulty',
            field=models.TextField(choices=[('', '---------'), (1, 'low'), (2, 'medium'), (3, 'high')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='levelquestion',
            name='option_create',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='levelquestion',
            name='que_format',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='levelquestion',
            name='question_inst',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='levelquestion',
            name='question_para',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='levelquestion',
            name='source',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='levelquestion',
            name='sub_concept',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='levelquestion',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='levelquestion',
            name='vocab_word',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='levelwords',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='levelquestion',
            name='question_genre',
            field=models.IntegerField(choices=[('', '---------'), (1, 'politics'), (9, 'tech'), (10, 'lifestyle'), (2, 'sports'), (3, 'science'), (4, 'entertainment'), (5, 'world'), (6, 'nation'), (7, 'environment'), (8, 'business and commerce'), (11, 'nature'), (12, 'others')]),
        ),
        migrations.AddField(
            model_name='offwords',
            name='level_word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.LevelWords'),
        ),
    ]
