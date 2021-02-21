from django.shortcuts import render
from .forms import KeyForm, InstanceForm, InstanceModelForm
from .models import KeyModel, InstanceModel
from .scriptbuilder import myfunc
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
        return render(request, 'instance.html', context)


def ShowInstance(request):
    mymodel = InstanceModel.objects.all()
    mykey = KeyModel.objects.get(id=1)
    context = {
        'model': mymodel
    }
    myfunc(mymodel, mykey)
    return render(request, 'showinstance.html', context)


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
        return render(request, 'editinstance.html', context)
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
    return render(request, 'duplicateinstance.html', context)


def DeleteInstance(request, n):

    if request.method == 'POST':
        InstanceModel.objects.get(name=n).delete()
        return render(request, 'home.html')

    instance = InstanceModel.objects.get(name=n)
    print(instance)
    context = {
        'instance': instance
    }
    return render(request, 'deleteinstance.html', context)


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
    elif n == 'plan':
        context = terraform_plan()
    elif n == 'apply':
        context = terraform_apply()
    elif n == 'destroy':
        context = terraform_destroy()
    else:
        context = {}
    return render(request, 'runscripts/terraform.html', context)
