# Generated by Django 4.0.1 on 2022-02-20 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muted', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_followers', to=settings.AUTH_USER_MODEL)),
                ('followed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_followes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(to='user_profile.Follow'),
        ),
    ]
