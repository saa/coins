# Generated by Django 2.0 on 2017-12-26 17:41

from django.db import migrations, models
import django.db.models.deletion
import django_db_constraints.operations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('owner', models.TextField()),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.TextField()),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('direction', models.TextField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='bank.Account')),
                ('from_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='bank.Account')),
                ('to_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='bank.Account')),
            ],
            options={
                'db_table': 'payments',
            },
        ),
        django_db_constraints.operations.AlterConstraints(
            name='Account',
            db_constraints={'positive_balance': 'check (balance >= 0)'},
        ),
    ]