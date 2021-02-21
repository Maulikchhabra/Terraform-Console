def myfunc(model, key):
    file = open("F:\\Python\\TerraformCode\\MyDjango\\infra\\src\\terraform\\main.tf", "w")
    written = 'provider \"aws\" {\n\tregion = \"' + key.region + '\"\n\taccess_key = \"' + key.accesskey + '\"\n\tsecret_key = \"' + key.secretaccesskey + '\"\n}\n\n'
    file.write(written)
    for m in model.all():
        written = "resource \"aws_instance\" " + m.name + " {\n" + "\tami = \"" + m.ami + "\"\n" + "\tinstance_type = \"" + m.instancetype + "\"\n" + "}\n\n"

        file.write(written)

    # print(written)
    file.close()
