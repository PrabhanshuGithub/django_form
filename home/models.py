from django.db import models
from django.contrib.auth.models import User  # Import User for password hashing

from django.utils import timezone
# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=128)  # Use a CharField with enough length for hashed passwords
    createdDate = models.DateTimeField(auto_now=True, null=True, default = timezone.now)
  

class Ticket(models.Model):
    fullname = models.CharField(max_length=20)
    email = models.ForeignKey(Contact, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now=True, null=True, default = timezone.now)
