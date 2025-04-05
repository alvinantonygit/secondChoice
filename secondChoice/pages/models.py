from django.db import models

# Create your models here.

class Teams(models.Model):
    first_name=models.CharField(max_length=255)
    lase_name=models.CharField(max_length=255)
    designation=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='photos/%y/%m/%d')
    facebook_link=models.URLField(max_length=100)
    twitterLink=models.URLField(max_length=100)
    google_page=models.URLField(max_length=100)
    created_date=models.DateTimeField(auto_now_add=True)


