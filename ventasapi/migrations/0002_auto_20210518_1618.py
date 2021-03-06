# Generated by Django 3.1.7 on 2021-05-18 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productosapi', '0001_initial'),
        ('ventasapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='cantidad',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='productosapi.productos', verbose_name='Producto'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='detalle',
            field=models.CharField(max_length=300, null=True, verbose_name='Detalle del pedido'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.DeleteModel(
            name='DetalleVenta',
        ),
    ]
