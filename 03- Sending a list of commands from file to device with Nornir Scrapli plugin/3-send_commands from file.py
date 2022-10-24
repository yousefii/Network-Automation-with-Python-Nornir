from nornir import InitNornir
from nornir_scrapli.tasks import send_commands_from_file
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file= "config.yaml")

result = nr.run(task=send_commands_from_file, file= "cmd-list.txt")
print_result(result)    
