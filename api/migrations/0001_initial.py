# Generated by Django 3.0.6 on 2020-05-12 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Errand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('finished', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
