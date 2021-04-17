# Generated by Django 2.2 on 2021-04-13 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('email', models.TextField()),
                ('password', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.TextField()),
                ('vendor_type', models.TextField()),
                ('vendor_id', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transportation_Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.TextField()),
                ('control_date', models.DateTimeField()),
                ('route_id', models.TextField()),
                ('miles', models.IntegerField()),
                ('milage_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('flat_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tractor_fuel_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('trailer_fuel_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('layover_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('yard_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('toll_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('detention_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('holiday_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('misc_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stop_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stop_count', models.IntegerField()),
                ('unload_hours', models.DecimalField(decimal_places=2, max_digits=10)),
                ('backhaul_credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('invoice_entered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entered_by', to='mlco_app.User')),
                ('venodor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_sender', to='mlco_app.Vendor')),
            ],
        ),
    ]