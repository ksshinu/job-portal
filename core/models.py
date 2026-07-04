from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class User(models.Model):
    user = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    email = models.EmailField(max_length=254, unique=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return f"User: {self.user}"

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    applied_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.user} - {self.job.title}"        