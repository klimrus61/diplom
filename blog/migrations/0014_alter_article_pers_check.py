# Generated by Django 4.0.4 on 2022-06-02 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_worker_user_alter_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pers_check',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.moderator'),
        ),
    ]
