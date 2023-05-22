import subprocess

secrets_management_tool = 'vault'
secrets_management_config_file = '/path/to/vault.hcl'

subprocess.call(['sudo', 'cp', secrets_management_config_file, '/etc/' + secrets_management_tool + '/'])
subprocess.call(['sudo', 'systemctl', 'restart', secrets_management_tool])
