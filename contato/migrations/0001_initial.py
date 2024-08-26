# Generated by Django 5.1 on 2024-08-23 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id_pessoa', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField()),
                ('idade', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]