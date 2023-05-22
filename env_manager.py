import subprocess

dependency_management_tool = 'pip'
dependency_management_config_file = '/path/to/pip.conf'

subprocess.call(['sudo', 'cp', dependency_management_config_file, '/etc/' + dependency_management_tool + '/'])
