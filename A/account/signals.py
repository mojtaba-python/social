from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import profile


def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile.objects.create(user=kwargs['instance'])

post_save.connect(receiver=create_profile, sender=User)