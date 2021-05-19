import json
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.forms.models import model_to_dict


class Post(models.Model):
    text = models.TextField()
    likes = models.IntegerField(default=0)


@receiver(post_save, sender=Post)
def notify_new_post(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "posts",
            {
                "type": "new.post",
                "data": json.dumps(model_to_dict(instance))
            }
        )
