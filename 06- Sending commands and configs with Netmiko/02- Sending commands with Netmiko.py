from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
commands=["show ip int brief | in up", "show version | inc Uptime"]

def netmiko_send_commands_example(task):
    for command in commands:
        task.run(task=netmiko_send_command, command_string=command)

results=nr.run(task=netmiko_send_commands_example)
print_result(results)
