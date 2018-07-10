# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-10 05:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('society', '0003_auto_20180710_0432'),
        ('accounts', '0002_auto_20180710_0431'),
        ('visitors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_visitor', models.CharField(max_length=2, verbose_name='No. Of Visitor')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('check_in', models.DateTimeField(auto_now_add=True, verbose_name='Check In Time')),
                ('check_out', models.DateTimeField(blank=True, null=True, verbose_name='Check out Time')),
                ('flat_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visit_flat', to='accounts.FlatDetail', verbose_name='flat_number')),
                ('society', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitor_society', to='society.Society', verbose_name='society')),
            ],
            options={
                'verbose_name': 'Visit Info',
                'verbose_name_plural': 'Visit Info',
            },
        ),
        migrations.RemoveField(
            model_name='visitor',
            name='check_in',
        ),
        migrations.RemoveField(
            model_name='visitor',
            name='check_out',
        ),
        migrations.RemoveField(
            model_name='visitor',
            name='flat_number',
        ),
        migrations.RemoveField(
            model_name='visitor',
            name='number_of_visitor',
        ),
        migrations.RemoveField(
            model_name='visitor',
            name='society',
        ),
        migrations.AddField(
            model_name='visitinfo',
            name='visitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitors.Visitor', verbose_name='Visitor'),
        ),
    ]