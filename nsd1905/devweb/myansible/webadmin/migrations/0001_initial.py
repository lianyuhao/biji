# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-10-29 11:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Argument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arg_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=50)),
                ('ip_addr', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modulename', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='host',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webadmin.HostGroup'),
        ),
        migrations.AddField(
            model_name='argument',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webadmin.Module'),
        ),
    ]