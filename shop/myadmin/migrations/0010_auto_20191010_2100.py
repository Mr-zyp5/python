# Generated by Django 2.1 on 2019-10-10 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0009_auto_20191010_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('sheng', models.CharField(max_length=100)),
                ('shi', models.CharField(max_length=100)),
                ('xian', models.CharField(max_length=100)),
                ('addinfo', models.CharField(max_length=255)),
                ('isselect', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.IntegerField(default=1570712415),
        ),
    ]