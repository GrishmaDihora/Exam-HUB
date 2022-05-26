from django.db import models

# Create your models here.
class Feedback(models.Model):
    query = models.CharField(max_length=800)
    cust_name = models.CharField(max_length=200)
    cust_email = models.CharField(max_length=200)
    cust_id = models.CharField(max_length=20, primary_key=True)