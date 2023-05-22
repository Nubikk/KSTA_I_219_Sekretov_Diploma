import subprocess

nginx_conf_file = '/path/to/nginx.conf'

subprocess.call(['sudo', 'cp', nginx_conf_file, '/etc/nginx/sites-available/'])
subprocess.call(['sudo', 'ln', '-s', '/etc/nginx/sites-available/nginx.conf', '/etc/nginx/sites-enabled/'])
subprocess.call(['sudo', 'nginx', '-t'])
subprocess.call(['sudo', 'systemctl', 'reload', 'nginx'])
