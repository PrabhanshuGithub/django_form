from django.contrib import admin
from home.models import Contact
from home.models import Ticket
# Register your models here.


admin.site.register(Ticket)
admin.site.register(Contact)