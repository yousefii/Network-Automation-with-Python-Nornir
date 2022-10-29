from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def napalm_get_example(task):
    task.run(task=napalm_get, getters=["get_interfaces_ip", "get_facts"])
#gatters info --> : https://napalm.readthedocs.io/en/latest/support/
results=nr.run(task=napalm_get_example)
print_result(results)
