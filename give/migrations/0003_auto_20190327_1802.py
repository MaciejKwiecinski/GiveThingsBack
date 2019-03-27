# Generated by Django 2.1.7 on 2019-03-27 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('give', '0002_auto_20190325_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='gifts',
            name='institution',
        ),
        migrations.RemoveField(
            model_name='gifts',
            name='localization',
        ),
        migrations.AlterField(
            model_name='gifts',
            name='type',
            field=models.IntegerField(choices=[(3, 'kasiążki'), (1, 'ubrania, do wyrzucenia'), (4, 'inne'), (2, 'zabawki'), (0, 'ubrania, które nadają się do użytku')]),
        ),
    ]
