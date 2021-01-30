from django.contrib import admin

from .models import Name, Id, Address
admin.site.register(Name)
admin.site.register(Id)
admin.site.register(Address)
# Register your models here.
