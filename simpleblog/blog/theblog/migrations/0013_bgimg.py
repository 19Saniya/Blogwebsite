# Generated by Django 4.2.5 on 2023-09-28 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0012_post_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='BgImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='bgimg')),
            ],
        ),
    ]
