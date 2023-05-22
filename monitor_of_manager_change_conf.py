import subprocess

monitoring_tool = 'etcd'
monitoring_config_file = '/path/to/etcd.conf'

subprocess.call(['sudo', 'cp', monitoring_config_file, '/etc/' + monitoring_tool + '/'])
subprocess.call(['sudo', 'systemctl', 'restart', monitoring_tool])
