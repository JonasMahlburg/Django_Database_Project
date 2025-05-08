from django.db import models

# Create your models here.
class Customer(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  newsletter_abo = models.BooleanField(default=True)
  email_address = models.EmailField(max_length=30, blank=True, default="")
  account = models.FloatField(blank=True, null=True)