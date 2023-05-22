import subprocess

monitoring_tool = 'rabbitmq'
monitoring_config_file = '/path/to/rabbitmq.conf'

subprocess.call(['sudo', 'cp', monitoring_config_file, '/etc/' + monitoring_tool + '/'])
subprocess.call(['sudo', 'systemctl', 'restart', monitoring_tool])
