from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
commands=["line console 0", "login local", "exec-timeout 600"]


def netmiko_send_config_exmaple(task):
    task.run(task=netmiko_send_config, config_commands=commands)

results=nr.run(task=netmiko_send_config_exmaple)
print_result(results)
