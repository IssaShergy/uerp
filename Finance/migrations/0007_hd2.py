# Generated by Django 2.2.10 on 2020-04-24 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0006_hh2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trantablemain',
            name='TranNo',
            field=models.BigIntegerField(default=0, verbose_name='رقم القيد'),
            preserve_default=False,
        ),
    ]
