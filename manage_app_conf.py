import subprocess

config_management_tool = 'ansible'
config_management_config_file = '/path/to/ansible.cfg'

subprocess.call(['sudo', 'cp', config_management_config_file, '/etc/' + config_management_tool + '/'])
subprocess.call(['sudo', 'systemctl', 'restart', config_management_tool])
