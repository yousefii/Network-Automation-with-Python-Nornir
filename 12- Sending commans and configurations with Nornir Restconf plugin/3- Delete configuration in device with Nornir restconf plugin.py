import requests
import json
from nornir import InitNornir
from rich import print as rprint
from nornir_utils.plugins.functions import print_result

requests.packages.urllib3.disable_warnings()

nr = InitNornir(config_file="config.yaml")

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}


def restconf_configuration_nornir_example(task):

    module = "Cisco-IOS-XE-native:native/router/router-ospf/ospf"
    url = f"https://{task.host.hostname}:443/restconf/data/{module}/process-id=1"


    response = requests.delete(url, headers=headers, auth=(f"{task.host.username}", f"{task.host.password}"), verify=False)
    print(response)

result = nr.run(task=restconf_configuration_nornir_example)
print_result(result)
