import os
import subprocess
import re


def terraform_init():
    os.chdir('D:\Minor 2\Demo\MyDjango\infra\src\\terraform')
    output = subprocess.run('terraform init', shell=True, capture_output=True, text=True)
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    result1 = ansi_escape.sub('', output.stdout)
    result2 = ansi_escape.sub('', output.stderr)

    cont = {
        'stdout': result1,
        'stderr': result2,
        'returncode': output.returncode,
    }

    return cont


def terraform_plan():
    os.chdir('D:\Minor 2\Demo\MyDjango\infra\src\\terraform')
    output = subprocess.run('terraform plan', shell=True, capture_output=True, text=True)
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    result1 = ansi_escape.sub('', output.stdout)
    result2 = ansi_escape.sub('', output.stderr)

    cont = {
        'stdout': result1,
        'stderr': result2,
        'returncode': output.returncode,
    }

    return cont


def terraform_apply():
    os.chdir('D:\Minor 2\Demo\MyDjango\infra\src\\terraform')
    output = subprocess.run('terraform apply -auto-approve', shell=True, capture_output=True, text=True)
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    result1 = ansi_escape.sub('', output.stdout)
    result2 = ansi_escape.sub('', output.stderr)

    cont = {
        'stdout': result1,
        'stderr': result2,
        'returncode': output.returncode,
    }

    return cont


def terraform_destroy():
    os.chdir('D:\Minor 2\Demo\MyDjango\infra\src\\terraform')
    output = subprocess.run('terraform destroy -auto-approve', shell=True, capture_output=True, text=True)
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    result1 = ansi_escape.sub('', output.stdout)
    result2 = ansi_escape.sub('', output.stderr)

    cont = {
        'stdout': result1,
        'stderr': result2,
        'returncode': output.returncode,
    }

    return cont
