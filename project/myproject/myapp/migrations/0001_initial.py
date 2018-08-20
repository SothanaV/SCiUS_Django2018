# Generated by Django 2.0.7 on 2018-08-20 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99)),
                ('lastname', models.CharField(max_length=99)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'None')], default='None', max_length=1)),
                ('Address', models.TextField()),
                ('tel', models.CharField(max_length=13)),
            ],
        ),
    ]