# Generated by Django 4.2.6 on 2023-12-28 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('email', models.EmailField(default='mounika@gmail.com', max_length=254)),
                ('topic_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.topic')),
            ],
        ),
    ]
