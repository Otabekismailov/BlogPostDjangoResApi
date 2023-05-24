# Generated by Django 4.2.1 on 2023-05-21 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_tag_type_alter_post_tag_alter_tag_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='type',
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(blank=True, choices=[('python', 'Python'), ('JAVA', 'Java'), ('javascript', 'Javascript')], null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='blog.tag'),
        ),
    ]
