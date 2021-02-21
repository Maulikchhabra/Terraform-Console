from django.contrib import admin
from .models import KeyModel, InstanceModel


# Register your models here.

admin.site.register(KeyModel)
admin.site.register(InstanceModel)