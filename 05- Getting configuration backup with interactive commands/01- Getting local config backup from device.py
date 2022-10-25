from nornir import InitNornir
from nornir_scrapli.tasks import send_interactive
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def interactive_commands_exmple(task):
    interact_lists=[
        
        ("copy running-config flash:backup", "Destination filename [backup]?", False),
        ("\n", f"{task.host}#", False)
    ]
    task.run(task=send_interactive, interact_events=interact_lists)

results=nr.run(task=interactive_commands_exmple)
print_result(results)
