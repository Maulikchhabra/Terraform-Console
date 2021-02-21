from django.urls import path
from .views import Home, Key, ShowKey, Instance, ShowInstance, EditInstance, DuplicateInstance, DeleteInstance, RunScripts, RunTerraform

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
]