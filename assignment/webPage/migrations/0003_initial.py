# Generated by Django 5.0.1 on 2024-09-25 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('webPage', '0002_delete_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('Address', models.CharField(max_length=500)),
                ('MobNO', models.CharField(max_length=11)),
            ],
        ),
    ]
