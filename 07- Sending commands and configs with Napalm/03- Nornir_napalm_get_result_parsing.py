from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from rich import print as rprint


nr = InitNornir(config_file="config.yaml")

def napalm_get_example(task):
    interfaces=task.run(task=napalm_get, getters=["get_interfaces"])


#    print(interfaces.result) #print mamoolie result
#    rprint(interfaces.result) #print sazmanyafte tar ba rprint 

    rprint(interfaces.result["get_interfaces"])


#    rprint(interfaces.result["get_interfaces"]["GigabitEthernet1"])


#    rprint(interfaces.result["get_interfaces"]["GigabitEthernet1"]["is_enabled"])




results=nr.run(task=napalm_get_example)
