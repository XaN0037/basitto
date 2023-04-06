# Generated by Django 4.1.7 on 2023-04-03 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0024_alter_discount_baget_alter_discount_dori_apparat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='baget',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.baget'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='dori_apparat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.doriaparat'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='kalso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.kalso'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='karniz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.karniz'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='karona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.karona'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='noj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.noj'),
        ),
    ]