# Generated by Django 2.2.10 on 2020-04-18 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0005_hh1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trantable',
            name='Ccenter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Finance.costcenter'),
        ),
    ]