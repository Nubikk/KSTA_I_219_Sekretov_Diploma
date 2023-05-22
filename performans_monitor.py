import subprocess

monitoring_tool = 'datadog'
monitoring_config_file = '/path/to/datadog.yml'

subprocess.call(['sudo', 'cp', monitoring_config_file, '/etc/' + monitoring_tool + '/'])
subprocess.call(['sudo', 'systemctl', 'restart', monitoring_tool])
