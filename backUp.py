import subprocess

backup_dir = '/path/to/backups'
app_dir = '/path/to/app'

subprocess.call(['sudo', 'tar', '-czvf', backup_dir + '/app-backup.tar.gz', app_dir])
