# Generated by Django 4.2.5 on 2023-09-04 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEscuela', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
            ],
        ),
    ]