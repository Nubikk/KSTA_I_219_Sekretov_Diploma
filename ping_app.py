import subprocess

monitoring_tool = 'pingdom'
monitoring_config_file = '/path/to/pingdom.yaml'

subprocess.call(['sudo', 'cp', monitoring_config_file, '/etc/' + monitoring_tool + '/'])
subprocess.call(['sudo', 'systemctl', 'restart', monitoring_tool])
