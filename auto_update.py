import subprocess

app_dir = '/path/to/app'
update_script = '/path/to/update.sh'

# Добавить скрипт обновления в crontab
subprocess.call(['echo', '0 0 * * 0', update_script, '>>', '/etc/crontab'])

# Создать скрипт обновления
with open(update_script, 'w') as f:
    f.write('#!/bin/bash\n')
    f.write('cd ' + app_dir + '\n')
    f.write('git pull\n')
    f.write('systemctl restart myapp\n')

subprocess.call(['sudo', 'chmod', '+x', update_script])
