# Generated by Django 3.2.2 on 2021-05-10 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('hours_available', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteers.volunteer')),
            ],
            options={
                'verbose_name_plural': 'VolunteerHours',
            },
        ),
    ]
