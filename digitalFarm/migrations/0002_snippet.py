# Generated by Django 3.1 on 2020-09-04 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalFarm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('created', models.DateTimeField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]