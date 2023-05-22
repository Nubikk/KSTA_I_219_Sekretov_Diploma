import subprocess

logging_tool = 'logrotate'
logging_config_file = '/path/to/logrotate.conf'

subprocess.call(['sudo', 'cp', logging_config_file, '/etc/' + logging_tool + '/'])
subprocess.call(['sudo', 'systemctl', 'restart', logging_tool])
