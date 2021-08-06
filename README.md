# Terraform Console

Terraform is a famous Infrastructure as a Code (IaaS) utility through which we can provision infrastructure by using the terraform configuration file.

The configuration file has a predefined syntax which has to be followed to get the desired infrastructure.

A web based console for Terraform Command Line utility.

The project uses Django to update the Terraform configuration file as per the services selected by the user on the web console and Terraform as a result sends the request to the cloud provider for provisioning the infrastructure specified.

#Tech Stack

1. Python (Django framework)
2. Grafana
3. Prometheus
4. Terraform

#Cloud Providers

Amazon Web Services is currently used as the cloud provider for the provisioning.
