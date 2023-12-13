from django.db import models
from django.core.validators import URLValidator, EmailValidator

# Create your models here.


class Personal_info(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_position = models.CharField()
    email = models.EmailField(validators=[EmailValidator])
    phone = models. CharField(max_length=20)
    website = models.URLField(validators=[URLValidator])
    short_info_about = models.TextField(max_length=1000, blank=True, null=True)
    about_skills = models.TextField(max_length=1000, blank=True, null=True)
    short_resume = models.TextField(max_length=1000, blank=True, null=True)
    about_certificates = models.TextField(
        max_length=1000, blank=True, null=True)
    about_services = models.TextField(max_length=1000, blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)


class Skill(models.Model):
    pass


class Education(models.Model):
    pass


class Experience(models.Model):
    pass


class Certificate(models.Model):
    pass


class Service(models.Model):
    pass


class Testimonial(models.Model):
    pass
