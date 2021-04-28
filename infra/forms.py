from django import forms
from django.forms import ModelForm
from .models import InstanceModel, VPCModel, SubnetModel, NetworkInterfaceModel


class KeyForm(forms.Form):
    author = forms.CharField(label='Author', max_length=100)
    accesskey = forms.CharField(label='Access Key', max_length=100)
    secretaccesskey = forms.CharField(label='Secret Access Key', max_length=100)
    region = forms.CharField(label='Region', max_length=100)


# class InstanceForm(forms.Form):
#     name = forms.CharField(label='Instance Name', max_length=100)
#     ami = forms.CharField(label='Instance AMI', max_length=100)
#     instancetype = forms.CharField(label='Instance Type', max_length=100)


class InstanceModelForm(ModelForm):
    class Meta:
        model = InstanceModel
        fields = ['name', 'ami', 'instancetype', 'netint']

        AmiChoices = (
            ('ami-0885b1f6bd170450c', 'Ubuntu "us-east-1"'),
            ('BYXTA', 'Ubuntu 2'),
            ('CXYZA', 'Ubuntu 3'),
        )

        InstanceTypeChoices = (
            ('t2.micro', 't2.micro'),
            ('t2.macro', 't2.macro'),
            ('t3.micro', 't3.micro'),
            ('t3.macro', 't3.macro'),
        )

        widgets = {
            # 'name': forms.CharField(attrs={
            #     'class': 'form-control'
            # }),
            'ami': forms.Select(choices=AmiChoices, attrs={'class': 'form-control'}),
            'instancetype': forms.Select(choices=InstanceTypeChoices, attrs={'class': 'form-control'}),
            # 'instancetype': forms.CharField(attrs={
            #     'class': 'form-control'
            # }),
        }


class VPCModelForm(ModelForm):
    class Meta:
        model = VPCModel
        fields = ['name', 'cidrblock']


class SubnetModelForm(ModelForm):
    class Meta:
        model = SubnetModel
        fields = ['name', 'vpcid', 'cidrblock']


class NetworkInterfaceModelForm(ModelForm):
    class Meta:
        model = NetworkInterfaceModel
        fields = ['name', 'subnetid', 'privateips']