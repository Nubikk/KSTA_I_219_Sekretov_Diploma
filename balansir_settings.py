import subprocess

backend1 = '10.0.0.1:8000'
backend2 = '10.0.0.2:8000'
virtual_ip = '10.0.0.100'

subprocess.call(['sudo', 'ip', 'addr', 'add', virtual_ip, 'dev', 'eth0'])
subprocess.call(['sudo', 'ip', 'route', 'add', virtual_ip, 'via', '10.0.0.1'])
subprocess.call(['sudo', 'iptables', '-t', 'nat', '-I', 'PREROUTING', '-d', virtual_ip, '-p', 'tcp', '--dport', '80', '-j', 'DNAT', '--to-destination', backend1])
subprocess.call(['sudo', 'iptables', '-t', 'nat', '-I', 'PREROUTING', '-d', virtual_ip, '-p', 'tcp', '--dport', '80', '-j', 'DNAT', '--to-destination', backend2])
subprocess.call(['sudo', 'iptables', '-t', 'nat', '-I', 'POSTROUTING', '-d', backend1, '-p', 'tcp', '--dport', '80', '-j', 'SNAT', '--to-source', virtual_ip])
subprocess.call(['sudo', 'iptables', '-t', 'nat', '-I', 'POSTROUTING', '-d', backend2, '-p', 'tcp', '--dport', '80', '-j', 'SNAT', '--to-source', virtual_ip])
