from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Product)
admin.site.register(models.Contact)
admin.site.register(models.Order)
admin.site.register(models.OrderUpdate)

