# Generated by Django 3.1 on 2020-09-06 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalFarm', '0003_auto_20200906_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(choices=[('Fruits', 'Veggies'), ('Nuts', 'Honey'), ('Tea', 'Legumes'), ('Oil', 'Wheat'), ('Flowers', 'Mushroom')], max_length=15, to='digitalFarm.Category'),
        ),
    ]
