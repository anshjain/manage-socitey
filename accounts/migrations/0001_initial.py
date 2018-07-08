# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-08 18:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('society', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat_number', models.CharField(max_length=255, verbose_name='Flat Number')),
                ('status', models.CharField(choices=[('Owned', 'Owned'), ('Rented', 'Rented'), ('Empty', 'Empty')], default='Owned', max_length=9)),
            ],
            options={
                'verbose_name': 'Flat Detail',
                'verbose_name_plural': 'Flat Details',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Member Name')),
                ('phone_number', models.CharField(max_length=10, verbose_name='phone number')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
            ],
            options={
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
            },
        ),
        migrations.CreateModel(
            name='MemberType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Member type',
                'verbose_name_plural': 'Member types',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('society', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_society', to='society.Society', verbose_name='society')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
        ),
        migrations.AddField(
            model_name='member',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membertypes', to='accounts.MemberType', verbose_name='type'),
        ),
        migrations.AddField(
            model_name='flatdetail',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owners', to='accounts.Member', verbose_name='owner'),
        ),
        migrations.AddField(
            model_name='flatdetail',
            name='society',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flat_society', to='society.Society', verbose_name='society'),
        ),
        migrations.AddField(
            model_name='flatdetail',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tenants', to='accounts.Member', verbose_name='tenant'),
        ),
    ]