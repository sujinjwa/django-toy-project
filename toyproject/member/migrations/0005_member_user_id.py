# Generated by Django 4.1.5 on 2023-01-26 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_remove_member_user_id_remove_member_user_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='user_id',
            field=models.CharField(blank=True, max_length=128, unique=True, verbose_name='아이디'),
        ),
    ]
