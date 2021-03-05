from django.shortcuts import render
from .forms import KeyForm, InstanceModelForm, VPCModelForm, SubnetModelForm, NetworkInterfaceModelForm
from .models import KeyModel, InstanceModel, VPCModel, SubnetModel, NetworkInterfaceModel
from .scriptbuilder import createScript
from .runterminal import *


# Create your views here.

def Home(request):
    return render(request, 'home.html')


def Key(request):
    if request.method == 'POST':
        form = KeyForm(request.POST)
        if form.is_valid():
            keyModel = KeyModel(author=form.cleaned_data['author'],
                                accesskey=form.cleaned_data['accesskey'],
                                secretaccesskey=form.cleaned_data['secretaccesskey'],
                                region=form.cleaned_data['region'], )
            keyModel.save()
            return render(request, 'home.html')
    else:
        form = KeyForm()
        context = {
            'form': form,
        }
        return render(request, 'key.html', context)


def ShowKey(request):
    mymodel = KeyModel.objects.all()

    context = {
        'model': mymodel
    }
    return render(request, 'showkey.html', context)


def Instance(request):
    if request.method == 'POST':
        form = InstanceModelForm(request.POST)
        # if form.is_valid():
        #     instanceModel = InstanceModel(name=form.cleaned_data['name'],
        #                         ami=form.cleaned_data['ami'],
        #                         instancetype=form.cleaned_data['instancetype'],
        #                         )
        #     instanceModel.save()
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = InstanceModelForm()
        context = {
            'form': form,
        }
        return render(request, 'instance/instance.html', context)


def ShowInstance(request):
    mymodel = InstanceModel.objects.all()
    mykey = KeyModel.objects.get(id=1)
    context = {
        'model': mymodel
    }
    # myfunc(mymodel, mykey)
    return render(request, 'instance/showinstance.html', context)


def EditInstance(request, n):
    if request.method == 'POST':
        instance = InstanceModel.objects.get(name=n)
        form = InstanceModelForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        return render(request, 'home.html')

    else:
        instance = InstanceModel.objects.get(name=n)
        form = InstanceModelForm(instance=instance)
        context ={
            'instance': form
        }
        return render(request, 'instance/editinstance.html', context)
    # instance = InstanceModel.objects.get(name=n)
    # print(instance)
    # context = {
    #     'instance': instance
    # }
    # return render(request, 'editinstance.html', context)


def DuplicateInstance(request, n):

    if request.method == 'POST':
        instance = InstanceModel.objects.get(name=n)
        form = InstanceModelForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'home.html')

    instance = InstanceModel.objects.get(name=n)
    form = InstanceModelForm(instance=instance)
    context ={
        'instance': form
    }
    return render(request, 'instance/duplicateinstance.html', context)


def DeleteInstance(request, n):

    if request.method == 'POST':
        InstanceModel.objects.get(name=n).delete()
        return render(request, 'home.html')

    instance = InstanceModel.objects.get(name=n)
    print(instance)
    context = {
        'instance': instance
    }
    return render(request, 'instance/deleteinstance.html', context)


def RunScripts(request):
    if request.method == 'POST':
        context = terraform_plan()
        return render(request, 'runscripts/demopage.html', context)
    else:
        return render(request, 'runscripts/demopage.html')


def RunTerraform(request, n):

    context = {}
    if n == 'init':
        context = terraform_init()
        print(context)
    elif n == 'plan':
        context = terraform_plan()
        print(context)
    elif n == 'apply':
        context = terraform_apply()
        print(context)
    elif n == 'destroy':
        context = terraform_destroy()
        print(context)
    else:
        context = {}
        myvpc = VPCModel.objects.all()
        mysubnet = SubnetModel.objects.all()
        mynetint = NetworkInterfaceModel.objects.all()
        mymodel = InstanceModel.objects.all()
        mykey = KeyModel.objects.get(id=1)
        createScript(myvpc, mysubnet, mynetint, mymodel, mykey)
    return render(request, 'runscripts/terraform.html', context)


def VPC(request):
    if request.method == 'POST':
        form = VPCModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = VPCModelForm()
        context = {
            'form': form,
        }
        return render(request, 'networking/vpc/vpc.html', context)
    # return render(request, 'networking/vpc.html')


def ShowNetworks(request):
    vpc = VPCModel.objects.all()
    subnet = SubnetModel.objects.all()
    networkinterface = NetworkInterfaceModel.objects.all()

    context = {
        'vpc': vpc,
        'subnet': subnet,
        'networkinterface': networkinterface,
    }
    return render(request, 'networking/show.html', context)


def Subnet(request):
    if request.method == 'POST':
        form = SubnetModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = SubnetModelForm()
        context = {
            'form': form,
        }
        return render(request, 'networking/subnet/subnet.html', context)
    # return render(request, 'networking/vpc.html')



def NetworkInterface(request):
    if request.method == 'POST':
        form = NetworkInterfaceModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = NetworkInterfaceModelForm()
        context = {
            'form': form,
        }
        return render(request, 'networking/netint/interface.html', context)
    # return render(request, 'networking/vpc.html')


def EditVPC(request, n):
    if request.method == 'POST':
        instance = VPCModel.objects.get(name=n)
        form = VPCModelForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        return render(request, 'home.html')

    else:
        instance = VPCModel.objects.get(name=n)
        form = VPCModelForm(instance=instance)
        context ={
            'instance': form
        }
        return render(request, 'networking/vpc/editvpc.html', context)


def DuplicateVPC(request, n):
    if request.method == 'POST':
        instance = VPCModel.objects.get(name=n)
        form = VPCModelForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'home.html')

    instance = VPCModel.objects.get(name=n)
    form = VPCModelForm(instance=instance)
    context ={
        'instance': form
    }
    return render(request, 'networking/vpc/duplicatevpc.html', context)



def DeleteVPC(request, n):
    if request.method == 'POST':
        VPCModel.objects.get(name=n).delete()
        return render(request, 'home.html')

    instance = VPCModel.objects.get(name=n)
    context = {
        'instance': instance
    }
    return render(request, 'networking/vpc/deletevpc.html', context)


def EditSubnet(request, n):
    if request.method == 'POST':
        instance = SubnetModel.objects.get(name=n)
        form = SubnetModelForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        return render(request, 'home.html')

    else:
        instance = SubnetModel.objects.get(name=n)
        form = SubnetModelForm(instance=instance)
        context ={
            'instance': form
        }
        return render(request, 'networking/subnet/editsubnet.html', context)


def DuplicateSubnet(request, n):
    if request.method == 'POST':
        instance = SubnetModel.objects.get(name=n)
        form = SubnetModelForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'home.html')

    instance = SubnetModel.objects.get(name=n)
    form = SubnetModelForm(instance=instance)
    context = {
        'instance': form
    }
    return render(request, 'networking/subnet/duplicatesubnet.html', context)


def DeleteSubnet(request, n):
    if request.method == 'POST':
        SubnetModel.objects.get(name=n).delete()
        return render(request, 'home.html')

    instance = SubnetModel.objects.get(name=n)
    context = {
        'instance': instance
    }
    return render(request, 'networking/subnet/deletesubnet.html', context)


def EditNetInt(request, n):
    if request.method == 'POST':
        instance = NetworkInterfaceModel.objects.get(name=n)
        form = NetworkInterfaceModelForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        return render(request, 'home.html')

    else:
        instance = NetworkInterfaceModel.objects.get(name=n)
        form = NetworkInterfaceModelForm(instance=instance)
        context ={
            'instance': form
        }
        return render(request, 'networking/netint/edit.html', context)


def DuplicateNetInt(request, n):
    if request.method == 'POST':
        instance = NetworkInterfaceModel.objects.get(name=n)
        form = NetworkInterfaceModelForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'home.html')

    instance = NetworkInterfaceModel.objects.get(name=n)
    form = NetworkInterfaceModelForm(instance=instance)
    context = {
        'instance': form
    }
    return render(request, 'networking/netint/duplicate.html', context)


def DeleteNetInt(request, n):
    if request.method == 'POST':
        NetworkInterfaceModel.objects.get(name=n).delete()
        return render(request, 'home.html')

    instance = NetworkInterfaceModel.objects.get(name=n)
    context = {
        'instance': instance
    }
    return render(request, 'networking/netint/delete.html', context)
