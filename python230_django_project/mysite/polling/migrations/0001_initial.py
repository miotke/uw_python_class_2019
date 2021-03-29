# Generated by Django 2.1.1 on 2019-11-03 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('text', models.TextField(blank=True)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]
