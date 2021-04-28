from django.contrib import admin
from .models import KeyModel, InstanceModel, VPCModel, SubnetModel, NetworkInterfaceModel


# Register your models here.

admin.site.register(KeyModel)
admin.site.register(InstanceModel)
admin.site.register(VPCModel)
admin.site.register(SubnetModel)
admin.site.register(NetworkInterfaceModel)
