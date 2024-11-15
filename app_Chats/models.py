from django.db import models


class ChatMessage(models.Model):
    user_image = models.ImageField(upload_to='chat_images/', blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True, null=True)
    system_response = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"User: {self.user_image} | System: {self.system_response}"
