from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, CandidateProfile, EmployerProfile

@receiver(post_save, sender=User)
def create_user_profile_signal(sender, instance, created, **kwargs):
    """
    Listens for user creation across the application and automatically 
    spins up the corresponding profile based on the registration role.
    """
    if created:
        if instance.role == User.CANDIDATE:
            CandidateProfile.objects.create(user=instance)
        elif instance.role == User.EMPLOYER:
            EmployerProfile.objects.create(user=instance)