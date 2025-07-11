from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class missingPerson(models.Model):
    missing_person_id=models.AutoField(primary_key=True)
    full_name=models.CharField(max_length=60)
    city=models.CharField(max_length=60)
    area=models.CharField(max_length=60)
    address=models.TextField()
    image=models.ImageField(upload_to="userfir/missingPerson")
    age=models.IntegerField(null=True, blank=True)
    mobile_no=models.CharField(max_length=13)
    description=models.CharField(max_length=100)
    user_role=models.CharField(max_length=100)
    height=models.IntegerField(null=True, blank=True)
    weight=models.IntegerField(null=True, blank=True)
    last_seen=models.CharField(max_length=100)
    police_station=models.CharField(max_length=100)
    status=models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)


    def image_tag(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.image.url))  # Get Image url

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

class FIR(models.Model):
    fir_id=models.AutoField(primary_key=True)
    police_station=models.CharField(max_length=100)
    user_proof=models.ImageField(upload_to="userfir/firProof")
    complaint_type=models.CharField(max_length=50)
    against_whom=models.CharField(max_length=50)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    def image_tag(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.user_proof.url))  # Get Image url

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

class criminal(models.Model):
    criminal_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=60)
    GEN = (('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER'))
    gender = models.CharField(max_length=200, choices=GEN)
    contact_no=models.CharField(max_length=13)
    address=models.TextField()
    city=models.CharField(max_length=60)
    area=models.CharField(max_length=60)
    image=models.ImageField(upload_to="userfir/criminal")
    email = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    description=models.CharField(max_length=100)
    status=models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)


    def image_tag(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.image.url))  # Get Image url

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True