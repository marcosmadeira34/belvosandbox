# Generated by Django 4.2.3 on 2023-07-26 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_id', models.CharField(max_length=100)),
                ('institution', models.CharField(max_length=100)),
            ],
        ),
    ]
