from django.db import models

# Create your models here.
class experience(models.Model):
    post = models.CharField(max_length = 30)
    company_name = models.CharField(max_length=30)
    desc = models.TextField()

class education(models.Model):
    university_name = models.CharField(max_length=30)
    degree_name = models.CharField(max_length=30)
    gpa = models.FloatField()
    date_text = models.CharField(max_length=30)

class awards(models.Model):
    achievement_name = models.CharField(max_length=50)
    cert_image = models.ImageField()

class project(models.Model):
    project_name = models.CharField(max_length=30)
    project_github = models.CharField(max_length=100)
    project_desc = models.TextField()