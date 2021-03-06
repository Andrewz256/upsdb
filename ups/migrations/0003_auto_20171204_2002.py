# Generated by Django 2.0 on 2017-12-04 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ups', '0002_auto_20171204_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battery',
            name='modBat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='ups.Modbat', to_field='modBat'),
        ),
        migrations.AlterField(
            model_name='battery',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='ups.State', to_field='stateUB'),
        ),
        migrations.AlterField(
            model_name='modbat',
            name='modBat',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='modups',
            name='modUps',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='stateUB',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='upsb',
            name='modUps',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='ups.Modups', to_field='modUps'),
        ),
        migrations.AlterField(
            model_name='upsb',
            name='obitN',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='upsb',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='ups.State', to_field='stateUB'),
        ),
    ]
