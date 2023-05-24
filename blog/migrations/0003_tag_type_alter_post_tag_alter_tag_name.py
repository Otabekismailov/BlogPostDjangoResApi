# Generated by Django 4.2.1 on 2023-05-21 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_tag_alter_tag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='type',
            field=models.CharField(choices=[('python', 'Python'), ('JAVA', 'Java'), ('javascript', 'Javascript')], default=None),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='blog.tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]