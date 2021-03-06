# Generated by Django 3.0.5 on 2020-05-03 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('attrs', models.TextField()),
            ],
            options={
                'verbose_name': 'Config',
                'verbose_name_plural': 'Configs',
            },
        ),
        migrations.CreateModel(
            name='Containers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('container_id', models.CharField(max_length=200)),
                ('labels', models.CharField(max_length=100)),
                ('name', models.UUIDField()),
                ('short_id', models.CharField(max_length=15)),
                ('status', models.SmallIntegerField()),
                ('attrs', models.TextField(max_length=100)),
            ],
            options={
                'verbose_name': 'Container',
                'verbose_name_plural': 'Containers',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('attrs', models.TextField()),
                ('image_id', models.CharField(max_length=100)),
                ('labels', models.CharField(max_length=100)),
                ('short_id', models.CharField(max_length=10)),
                ('tags', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Plugins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plugin_id', models.CharField(max_length=200)),
                ('short_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('enabled', models.BooleanField()),
                ('settings', models.TextField()),
                ('attrs', models.TextField()),
            ],
            options={
                'verbose_name': 'Plugin',
                'verbose_name_plural': 'Plugins',
            },
        ),
        migrations.CreateModel(
            name='Secrets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('attrs', models.TextField()),
            ],
            options={
                'verbose_name': 'Secret',
                'verbose_name_plural': 'Secrets',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.CharField(max_length=200)),
                ('short_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=100)),
                ('attrs', models.TextField(max_length=100)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Swarm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Volumes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume_id', models.CharField(max_length=200)),
                ('short_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('attrs', models.TextField()),
            ],
            options={
                'verbose_name': 'Volume',
                'verbose_name_plural': 'Volumes',
            },
        ),
        migrations.CreateModel(
            name='Networks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('network_id', models.CharField(max_length=100)),
                ('short_id', models.CharField(max_length=10)),
                ('attrs', models.TextField(max_length=100)),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='virtualization.Containers')),
            ],
            options={
                'verbose_name': 'Network',
                'verbose_name_plural': 'Networks',
            },
        ),
        migrations.AddField(
            model_name='containers',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='virtualization.Images'),
        ),
    ]
