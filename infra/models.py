from django.db import models


# Create your models here.



class KeyModel(models.Model):
    author = models.CharField(max_length=100)
    accesskey = models.CharField(max_length=100)
    secretaccesskey = models.CharField(max_length=100)
    region = models.CharField(max_length=20)

    def __str__(self):
        return self.author


class InstanceModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ami = models.CharField(max_length=100)
    instancetype = models.CharField(max_length=100)
    netint = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class VPCModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    cidrblock = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubnetModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    vpcid = models.CharField(max_length=100,)
    cidrblock = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class NetworkInterfaceModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subnetid = models.CharField(max_length=100)
    privateips = models.CharField(max_length=200)

    def __str__(self):
        return self.name