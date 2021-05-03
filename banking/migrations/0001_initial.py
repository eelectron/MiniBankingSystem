# Generated by Django 3.2 on 2021-05-03 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeOfAccount', models.CharField(max_length=128)),
                ('balance', models.DecimalField(decimal_places=4, max_digits=256)),
                ('interest', models.DecimalField(decimal_places=4, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=128)),
                ('lastName', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
                ('verificationStatus', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creationDate', models.DateTimeField()),
                ('typeOfTransaction', models.CharField(max_length=64)),
                ('balance', models.DecimalField(decimal_places=4, max_digits=256)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='banking.account')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line1', models.CharField(max_length=256)),
                ('line2', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=128)),
                ('pincode', models.IntegerField()),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='banking.customer')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='banking.customer'),
        ),
    ]
