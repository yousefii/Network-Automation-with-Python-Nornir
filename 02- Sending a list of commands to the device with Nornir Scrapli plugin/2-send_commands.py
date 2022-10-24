from nornir import InitNornir
from nornir_scrapli.tasks import send_commands
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file= "config.yaml")

result = nr.run(task=send_commands, commands=["show version | include Uptime" , "show ip int brief "])
print_result(result)    


