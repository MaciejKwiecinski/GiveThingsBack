# Generated by Django 2.1.7 on 2019-03-29 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('give', '0002_auto_20190329_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='quantity',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='phone',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='postcode',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='gifts',
            name='type',
            field=models.IntegerField(choices=[(3, 'kasiążki'), (1, 'ubrania, do wyrzucenia'), (2, 'zabawki'), (0, 'ubrania, które nadają się do użytku'), (4, 'inne')]),
        ),
    ]