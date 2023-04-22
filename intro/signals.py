from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
import logging

logger = logging.getLogger(__name__)

@receiver(user_logged_in)
def log_admin_login(sender, user, request, **kwargs):
    if user.is_staff or user.is_superuser:
        logger.info(f"Admin user {user.username} logged in from IP {request.META.get('REMOTE_ADDR')}")
