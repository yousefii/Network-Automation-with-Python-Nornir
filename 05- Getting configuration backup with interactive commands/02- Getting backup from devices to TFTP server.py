from nornir import InitNornir
from nornir_scrapli.tasks import send_interactive
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def interactive_commands_exmple(task):
    ip = "192.168.200.1"
    interact_lists=[
#insert your TFTP ip address instead 192.168.200.1       
        ("copy running-config tftp:", "Address or name of remote host []?", False),
        (ip, " ", False ),
        ("\n", f"{task.host}#", False)
        
    ]
    task.run(task=send_interactive, interact_events=interact_lists)

results=nr.run(task=interactive_commands_exmple)
print_result(results)

print("DONE !!! \n Saving backup in the TFTP server 192.168.200.1 is completed!")
