import subprocess

monitoring_tool = 'zabbix'
monitoring_config_file = '/path/to/zabbix_agentd.conf'

subprocess.call(['sudo', 'cp', monitoring_config_file, '/etc/' + monitoring_tool + '/'])
subprocess.call(['sudo', 'systemctl', 'restart', monitoring_tool])
