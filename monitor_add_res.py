import subprocess

monitoring_tool = 'sysdig'
monitoring_config_file = '/path/to/sysdig.yaml'

subprocess.call(['sudo', 'cp', monitoring_config_file, '/etc/' + monitoring_tool + '/'])
subprocess.call(['sudo', 'systemctl', 'restart', monitoring_tool])
