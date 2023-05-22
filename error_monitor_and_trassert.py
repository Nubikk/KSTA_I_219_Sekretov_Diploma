import subprocess

monitoring_tool = 'sentry'
monitoring_config_file = '/path/to/sentry.ini'

subprocess.call(['sudo', 'cp', monitoring_config_file, '/etc/' + monitoring_tool + '/'])
subprocess.call(['sudo', 'systemctl', 'restart', monitoring_tool])
