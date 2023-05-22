# Импортируем нужные библиотеки
import os
import subprocess

# Определяем путь к директории приложения
app_dir = '/path/to/app'

# Определяем команды для управления приложением
start_cmd = 'python app.py'
stop_cmd = 'killall python'

# Определяем функции для запуска и остановки приложения
def start_app():
    os.chdir(app_dir)
    subprocess.Popen(start_cmd, shell=True)

def stop_app():
    subprocess.Popen(stop_cmd, shell=True)

# Вызываем функции для запуска и остановки приложения
start_app()
# Для остановки приложения, раскомментируйте следующую строку
# stop_app()
