# Generated by Django 3.1.7 on 2022-03-06 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0003_auto_20200507_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='distributor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='facturacion.customer'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customerType',
            field=models.CharField(choices=[('Wholesale', 'Wholesale'), ('Retail', 'Retail'), ('Salesman', 'Salesman')], default='Salesman', max_length=10),
        ),
    ]