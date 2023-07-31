# Generated by Django 4.2.3 on 2023-07-31 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_requests'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=1, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default=1, upload_to='uploads/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='point',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
