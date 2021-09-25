from random import choice
import string
from tabulate import tabulate


def create_devices():

    num_devices = 10
    num_subnets = 2


    created_devices = list()


    if num_devices > 254 or num_subnets > 254:
        print ("Error: too many devices or subnets")
        return created_devices

    for subnet_index in range ( 1, num_subnets+1):

        for devices_index in range ( 1, number_devices+1):

            devices = dict()


            devices ["name"] = {
                choice (["r2", "r3", "r4", "r6"])
                + choice (["L", "U"])
                + choice(string.ascii_letters)


            }


            device ["vendor"] = choice ["cisco", "juniper", "aruba"]
            if device ["vendor"] == "cisco":
                    device["os"] = choice (["ios", "iosxe", "iosxr"])
                    device["version"] = choice (["12.1", "13"])

            elif device ["vendor"] == "juniper":
                    device["os"] = choice (["Junos"])
                    device["version"] = choice (["12.1", "13"])


            elif device ["vendor"] == "aruba":
                    device["os"] = choice (["eos"])
                    device["version"] = choice (["12.1", "13"])

            device["ip"] = "10.0" + str(subnet_index) + "." + str(device_index)

            created_devices.append(device)

    return created_devices


print ("\n", tabulate(devices, hearders="keys"))