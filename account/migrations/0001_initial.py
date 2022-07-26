# Generated by Django 4.0.4 on 2022-06-30 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='Email')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Username')),
                ('bio', models.TextField(verbose_name='Bio')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='is Active')),
                ('is_admin', models.BooleanField(default=False, verbose_name='is Admin')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is Staff')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='is Superuser')),
                ('profile_img', models.ImageField(blank=True, default='default.png', max_length=200, null=True, upload_to='profile_images/%y/%m/%d', verbose_name='Profile Image')),
                ('hide_email', models.BooleanField(default=True, verbose_name='Hide Email')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
