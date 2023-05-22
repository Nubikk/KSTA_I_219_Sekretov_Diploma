import subprocess

ssl_cert_file = '/path/to/ssl/cert'
ssl_key_file = '/path/to/ssl/key'

subprocess.call(['sudo', 'cp', ssl_cert_file, '/etc/ssl/certs/'])
subprocess.call(['sudo', 'cp', ssl_key_file, '/etc/ssl/private/'])
subprocess.call(['sudo', 'chmod', '600', '/etc/ssl/private/ssl.key'])
