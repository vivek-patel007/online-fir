from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.utils.safestring import mark_safe


class CustomUser(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_police = models.BooleanField(default=False)
    GEN = (('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER'))
    gender = models.CharField(max_length=200, choices=GEN)
    dob = models.DateField(null=True, blank=True)
    CIT = (('Rajkot', 'Rajcot'), ('Ahmedabad', 'Ahmedabad'), ('Visnagar', 'Visnagar'))
    city = models.CharField(max_length=200, choices=CIT)
    address = models.TextField()
    contact_no = models.CharField(max_length=13)
    image = models.ImageField(upload_to="home/UserImages")
    otp = models.IntegerField(null=True, blank=True)
    division = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)

    def image_tag(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.image.url))  # Get Image url

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class contactUs(models.Model):
    contact_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    msg = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.full_name

class feedback(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    email_id=models.CharField(max_length=100)
    message=models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.email_id