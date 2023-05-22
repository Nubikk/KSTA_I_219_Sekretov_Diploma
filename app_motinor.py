import subprocess

monitoring_tool = 'prometheus'
monitoring_config_file = '/path/to/prometheus.yml'

subprocess.call(['sudo', 'cp', monitoring_config_file, '/etc/' + monitoring_tool + '/'])
subprocess.call(['sudo', 'systemctl', 'restart', monitoring_tool])
