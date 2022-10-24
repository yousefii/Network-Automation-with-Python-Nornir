from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file= "config.yaml")

result = nr.run(task=send_command, command="show ip interface brief ")
print_result(result)    
