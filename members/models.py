from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    profile_image = models.ImageField(upload_to='member_profiles/', null=True, blank=True)

class Attendance(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    present = models.BooleanField(default=False)
    
class UnrecognizedFaceRecord(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    decision = models.TextField()
    image = models.ImageField(upload_to='unrecognized_faces/', null=True, blank=True)
    
class UploadedImage(models.Model):
    image = models.ImageField(upload_to='unrecognized_faces/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    
