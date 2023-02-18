# Generated by Django 4.1.7 on 2023-02-17 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='created',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='debt',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='title',
        ),
        migrations.RemoveField(
            model_name='products',
            name='created',
        ),
        migrations.RemoveField(
            model_name='products',
            name='debt',
        ),
        migrations.RemoveField(
            model_name='products',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='products',
            name='title',
        ),
        migrations.AddField(
            model_name='factory',
            name='contacts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='network.contacts'),
        ),
        migrations.AddField(
            model_name='factory',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='network.products'),
        ),
        migrations.AddField(
            model_name='ip',
            name='contacts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='network.contacts'),
        ),
        migrations.AddField(
            model_name='ip',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='network.products'),
        ),
        migrations.AddField(
            model_name='retailnetwork',
            name='contacts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='network.contacts'),
        ),
        migrations.AddField(
            model_name='retailnetwork',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='network.products'),
        ),
    ]
