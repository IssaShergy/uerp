# Generated by Django 2.2.10 on 2020-04-15 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0002_changed_my_model26'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactiontbl',
            name='tranmaster',
        ),
        migrations.DeleteModel(
            name='TModel',
        ),
        migrations.DeleteModel(
            name='transactionMaster',
        ),
        migrations.DeleteModel(
            name='transactiontbl',
        ),
    ]