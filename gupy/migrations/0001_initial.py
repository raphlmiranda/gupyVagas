# Generated by Django 3.1.2 on 2020-11-15 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='empresas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='vagas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('depart', models.CharField(max_length=30)),
                ('link', models.CharField(max_length=150)),
                ('data', models.DateField()),
                ('id_empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gupy.empresas')),
            ],
        ),
    ]
