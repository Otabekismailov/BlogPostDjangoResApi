# Generated by Django 4.2.1 on 2023-05-23 12:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_comment_is_active_comment_parent_comment_reviewed'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='likedislike',
            unique_together={('post', 'user')},
        ),
    ]
