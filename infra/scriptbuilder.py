# def myfunc(model, key):
#     file = open("D:\\Minor 2\\Demo\\MyDjango\\infra\\src\\terraform\\main.tf", "w")
#     written = 'provider \"aws\" {\n\tregion = \"' + key.region + '\"\n\taccess_key = \"' + key.accesskey + '\"\n\tsecret_key = \"' + key.secretaccesskey + '\"\n}\n\n'
#     file.write(written)
#     for m in model.all():
#         written = "resource \"aws_instance\" " + m.name + " {\n" + "\tami = \"" + m.ami + "\"\n" + "\tinstance_type = \"" + m.instancetype + "\"\n" + "}\n\n"
#
#         file.write(written)
#
#     # print(written)
#     file.close()


def createScript(vpc, subnet, netint, instance, key):
    file = open("D:\\Minor 2\\Demo\\MyDjango\\infra\\src\\terraform\\main.tf", "w")
    written = 'provider \"aws\" {\n\tregion = \"' + key.region + '\"\n\taccess_key = \"' + key.accesskey + '\"\n\tsecret_key = \"' + key.secretaccesskey + '\"\n}\n\n'
    file.write(written)


    for m in vpc.all():
        written = "resource \"aws_vpc\" \"" + m.name + "\" { \n" + "\tcidr_block = \"" + m.cidrblock + "\"\n" + "}\n\n"

        file.write(written)


    for m in subnet.all():
        written = "resource \"aws_subnet\" \"" + m.name + "\" {\n" + "\tvpc_id = aws_vpc." + m.vpcid + ".id\n" + "\tcidr_block = \"" + m.cidrblock + "\"\n" + "}\n\n"

        file.write(written)


    for m in netint.all():
        written = "resource \"aws_network_interface\" \"" + m.name + "\" {\n" + "\tsubnet_id = aws_subnet." + m.subnetid + ".id\n"+ "\tprivate_ips = " + m.privateips + "\n" + "}\n\n"

        file.write(written)


    for m in instance.all():
        written = "resource \"aws_instance\" \"" + m.name + "\" {\n" + "\tami = \"" + m.ami + "\"\n" + "\tinstance_type = \"" + m.instancetype + "\"\n"

        if m.netint:
            written = written + "\n\tnetwork_interface {\n\t\tnetwork_interface_id = aws_network_interface." + m.netint + ".id\n\t\tdevice_index = 0\n\t}\n\n"

        written = written + "}\n\n"
        file.write(written)


    # print(written)
    file.close()
