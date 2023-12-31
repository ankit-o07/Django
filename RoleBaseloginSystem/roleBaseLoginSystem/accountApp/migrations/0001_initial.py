# Generated by Django 4.2 on 2023-04-15 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=2)),
                ('bloodPressure', models.CharField(choices=[('H', 'High'), ('L', 'Low'), ('N', 'Normal')], max_length=2)),
                ('diabetes', models.CharField(choices=[('H', 'High'), ('L', 'Low'), ('N', 'Normal')], max_length=2)),
                ('Dob', models.DateField()),
                ('email', models.EmailField(max_length=200)),
                ('phoneNumber', models.IntegerField()),
                ('address', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
