import subprocess

tests_dir = '/path/to/tests'

subprocess.call(['python', '-m', 'unittest', 'discover', '-s', tests_dir])
