import subprocess

version_control_tool = 'git'
version_control_config_file = '/path/to/gitconfig'

subprocess.call(['sudo', 'cp', version_control_config_file, '/etc/' + version_control_tool + '/'])
