from django.urls import path
from .views import Home, Key, ShowKey, Instance, ShowInstance, EditInstance, DuplicateInstance, DeleteInstance, RunScripts, RunTerraform, VPC, ShowNetworks, Subnet, NetworkInterface, EditVPC, DeleteVPC, DuplicateVPC, EditSubnet, DeleteSubnet, DuplicateSubnet, EditNetInt, DuplicateNetInt, DeleteNetInt

urlpatterns = [
    path('home/', Home , name='HomePage'),
    path('key/', Key, name='KeyPage'),
    path('showkey/', ShowKey, name='ShowKeyPage'),
    path('instance/', Instance, name='InstancePage'),
    path('showinstance/', ShowInstance, name='ShowInstancePage'),
    path('editinstance/<str:n>', EditInstance, name='EditInstancePage'),
    path('duplicateinstance/<str:n>', DuplicateInstance, name='DuplicateInstancePage'),
    path('deleteinstance/<str:n>', DeleteInstance, name='DeleteInstancePage'),
    path('run/', RunScripts, name='RunScriptsPage'),
    path('terr/<str:n>', RunTerraform, name='RunTerraformPage'),
    path('networking/vpc', VPC, name='VPCPage'),
    path('networking/show', ShowNetworks, name='ShowNetworksPage'),
    path('networking/subnet', Subnet, name='SubnetPage'),
    path('networking/interface', NetworkInterface, name='NetworkInterfacePage'),
    path('networking/vpc/edit/<str:n>', EditVPC, name='EditVPCPage'),
    path('networking/vpc/duplicate/<str:n>', DuplicateVPC, name='DuplicateVPCPage'),
    path('networking/vpc/delete/<str:n>', DeleteVPC, name='DeleteVPCPage'),
    path('networking/subnet/edit/<str:n>', EditSubnet, name='EditSubnetPage'),
    path('networking/subnet/duplicate/<str:n>', DuplicateSubnet, name='DuplicateSubnetPage'),
    path('networking/subnet/delete/<str:n>', DeleteSubnet, name='DeleteSubnetPage'),
    path('networking/netint/edit/<str:n>', EditNetInt, name='EditNetworkInterfacePage'),
    path('networking/netint/duplicate/<str:n>', DuplicateNetInt, name='DuplicateNetworkInterfacePage'),
    path('networking/netint/delete/<str:n>', DeleteNetInt, name='DeleteNetworkInterfacePage'),
]