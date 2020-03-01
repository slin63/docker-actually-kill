import subprocess
import sys
import os

dir_ = os.path.dirname(os.path.realpath(__file__))
sound_command = f"mpg123 -q {dir_}/effect.mp3"

process = subprocess.Popen(f"docker kill {sys.argv[1]}".split(), stdout=subprocess.PIPE)
sound_process = subprocess.run(sound_command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
if output:
    print(output.decode('utf-8'))
