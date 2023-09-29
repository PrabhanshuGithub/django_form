from django.db import models
from django.contrib.auth.models import User  # Import User for password hashing

from django.utils import timezone
# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=128)  # Use a CharField with enough length for hashed passwords
    # createdDate = models.DateTimeField(auto_now=True, null=True, default = timezone.now)
  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    


TICKET_STATUS_CHOICES = [
    ('Awaiting', 'Awaiting'),
    ('Pending', 'Pending'),
    ('Closed', 'Closed'),
]


class Ticket(models.Model):
    fullname = models.CharField(max_length=20)
    email = models.ForeignKey(Contact, on_delete=models.CASCADE)
    # createdDate = models.DateTimeField(auto_now=True, null=True, default = timezone.now)
 
    concern = models.CharField(max_length=700, default= "")
    status = models.CharField(max_length=10, choices=TICKET_STATUS_CHOICES, default= "Awaiting")

    def __str__(self):
        return self.fullname
