# Generated by Django 4.0.4 on 2022-05-29 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_article_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_on']},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='pub_date',
            new_name='created_on',
        ),
    ]
