# Generated by Django 3.0.2 on 2020-01-12 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0001_initial'),
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.Card')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myauth.Profile')),
            ],
        ),
    ]
