# Generated by Django 2.0.1 on 2018-01-26 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('region', '0001_initial'),
        ('retailer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=256)),
                ('display_name', models.CharField(max_length=256)),
                ('tel', models.CharField(max_length=32, null=True)),
                ('address', models.CharField(max_length=512, null=True)),
                ('working_hours', models.CharField(max_length=512, null=True)),
                ('website', models.CharField(max_length=512, null=True)),
                ('email', models.CharField(max_length=128, null=True)),
                ('longitude', models.FloatField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stores', to='region.Region')),
                ('retailer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stores', to='retailer.Retailer')),
            ],
        ),
        migrations.CreateModel(
            name='StoreProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('value', models.CharField(blank=True, max_length=1024)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='store.Store')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
