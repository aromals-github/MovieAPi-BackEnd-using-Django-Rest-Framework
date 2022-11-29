# Generated by Django 4.1.3 on 2022-11-28 08:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='movies',
            new_name='movie',
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('user', 'movie')},
        ),
        migrations.AlterIndexTogether(
            name='rating',
            index_together={('user', 'movie')},
        ),
    ]