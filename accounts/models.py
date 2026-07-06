from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Define role constants
    ADMIN = 'admin'
    EMPLOYER = 'employer'
    CANDIDATE = 'candidate'
    
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (EMPLOYER, 'Employer'),
        (CANDIDATE, 'Candidate'),
    ]
    
    # Custom attributes required by assignment
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default=CANDIDATE)
    is_verified = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Use Email as the unique login parameter instead of a traditional username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Django requires username to remain in backend logs

    def __str__(self):
        return f"{self.email} ({self.role})"


class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidate_profile')
    skills = models.TextField(blank=True, null=True)
    experience_years = models.IntegerField(default=0)

    def __str__(self):
        return f"Candidate Profile: {self.user.email}"

class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer_profile')
    company_name = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Employer Profile: {self.user.email}"