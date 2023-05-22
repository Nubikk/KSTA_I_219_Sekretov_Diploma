import subprocess
unit_template = '''[Unit]
Description=My Application
After=network.target

[Service]
User=user
WorkingDirectory=/path/to/app
ExecStart=/usr/bin/python /path/to/app/app.py
Restart=always

[Install]
WantedBy=multi-user.target
'''

unit_file = '/etc/systemd/system/myapp.service'

with open(unit_file, 'w') as f:
    f.write(unit_template)

subprocess.call(['sudo', 'systemctl', 'daemon-reload'])
subprocess.call(['sudo', 'systemctl', 'enable', 'myapp'])
subprocess.call(['sudo', 'systemctl', 'start', 'myapp'])
