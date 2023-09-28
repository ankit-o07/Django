# Generated by Django 4.2 on 2023-04-16 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accountApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(blank=True, max_length=100)),
                ('userName', models.CharField(max_length=50)),
                ('Dob', models.DateField()),
                ('email', models.EmailField(max_length=200)),
                ('phoneNumber', models.IntegerField()),
                ('account_type', models.CharField(choices=[('p', 'Patient'), ('D', 'Doctor'), ('L', 'Laboratory'), ('P', 'pharmacy')], max_length=2)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Dob',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phoneNumber',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accountApp.userprofile'),
        ),
    ]
