import subprocess

public_ip = '203.0.113.1'
port = '8080'

subprocess.call(['sudo', 'iptables', '-I', 'INPUT', '1', '-p', 'tcp', '--dport', port, '-j', 'ACCEPT'])
subprocess.call(['sudo', 'iptables', '-I', 'OUTPUT', '1', '-p', 'tcp', '--sport', port, '-j', 'ACCEPT'])
subprocess.call(['sudo', 'iptables', '-t', 'nat', '-A', 'PREROUTING', '-p', 'tcp', '--dport', port, '-j', 'DNAT', '--to-destination', '127.0.0.1:8000'])
subprocess.call(['sudo', 'iptables', '-t', 'nat', '-A', 'POSTROUTING', '-p', 'tcp', '-d', '127.0.0.1', '--dport', '8000', '-j', 'SNAT', '--to-source', public_ip])
