# Generated by Django 5.1.2 on 2024-11-07 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Chats', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='user_message',
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='caption',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to='chat_images/'),
        ),
    ]