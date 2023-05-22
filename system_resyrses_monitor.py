import subprocess

monitoring_tool = 'grafana'
monitoring_config_file = '/path/to/grafana.ini'

subprocess.call(['sudo', 'cp', monitoring_config_file, '/etc/' + monitoring_tool + '/'])
subprocess.call(['sudo', 'systemctl', 'restart', monitoring_tool])
