# Generated by Django 4.2.6 on 2023-12-28 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_webpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessRecors',
            fields=[
                ('date', models.DateField()),
                ('author', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.webpage')),
            ],
        ),
    ]
