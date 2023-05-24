# Generated by Django 4.2.1 on 2023-05-21 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_type_alter_post_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='type',
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(blank=True, choices=[('python', 'Python'), ('JAVA', 'Java'), ('javascript', 'Javascript')], null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='blog.tag'),
        ),
    ]