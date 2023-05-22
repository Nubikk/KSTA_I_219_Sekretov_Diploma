import subprocess

security_tool = 'osquery'
security_config_file = '/path/to/osquery.conf'

subprocess.call(['sudo', 'cp', security_config_file, '/etc/' + security_tool + '/'])
subprocess.call(['sudo', 'systemctl', 'restart', security_tool])
