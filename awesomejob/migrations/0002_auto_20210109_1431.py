# Generated by Django 2.2.17 on 2021-01-09 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awesomejob', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fami_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('link', models.CharField(max_length=400)),
            ],
        ),
        migrations.RenameModel(
            old_name='jobs',
            new_name='awesome_job',
        ),
    ]
