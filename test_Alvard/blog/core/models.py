from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Blog(models.Model):
    BLOG_TYPES = (
        ("1", "Sport"),
        ("2", "Travel"),
        ("3", "Handmade"),
        ("4", "Funny Animals"),
        ("5", "Nature")
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    blog_type = models.CharField(choices=BLOG_TYPES, default="4", max_length=1)
    creation_date = models.DateField()
