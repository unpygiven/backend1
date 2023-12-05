# Generated by Django 4.2.7 on 2023-11-08 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('text', models.CharField(max_length=250)),
                ('video_link', models.CharField(max_length=250)),
                ('photo_link', models.CharField(max_length=250)),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
                ('publishedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
