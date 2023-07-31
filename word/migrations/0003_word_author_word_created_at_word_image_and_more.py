# Generated by Django 4.2.3 on 2023-07-31 22:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('word', '0002_word_age_word_content_word_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='word',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='word',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='word',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='word',
            name='views',
            field=models.IntegerField(default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='word',
            name='age',
            field=models.IntegerField(max_length=8),
        ),
        migrations.AlterField(
            model_name='word',
            name='content',
            field=models.TextField(max_length=32),
        ),
        migrations.AlterField(
            model_name='word',
            name='likes',
            field=models.ManyToManyField(null=True, related_name='like_word', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='word',
            name='title',
            field=models.IntegerField(max_length=16),
        ),
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('words', models.ManyToManyField(to='word.word')),
            ],
        ),
        migrations.CreateModel(
            name='Edit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('views', models.IntegerField(max_length=8)),
                ('content', models.TextField(max_length=32)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(null=True, related_name='like_edit', to=settings.AUTH_USER_MODEL)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='word.word')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(max_length=32)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('edit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='word.edit')),
                ('likes', models.ManyToManyField(null=True, related_name='like_comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
