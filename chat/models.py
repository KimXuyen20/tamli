from django.db import models

from accounts.models import Account

# Create your models here.
class ChatGroup(models.Model):

    group_name = models.CharField(max_length=128, unique=True, blank=True)



    def __str__(self):
        return self.group_name


class GroupMessage(models.Model):
    group = models.ForeignKey(ChatGroup, related_name='chat_messages', on_delete=models.CASCADE)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    body = models.CharField(max_length=300, blank=True, null=True)
    file = models.FileField(upload_to='files/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.body:
            return f'{self.author.full_name} : {self.body}'
        elif self.file:
            return f'{self.author.full_name} : {self.filename}'
    
    class Meta:
        ordering = ['-created']
    