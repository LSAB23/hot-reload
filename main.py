import os
import sys
import subprocess
import time
from pathlib import Path
from argparse import ArgumentParser
from dataclasses import dataclass
try:
    from colorama import init, Fore
except ImportError:
    def init(*args, **kwargs):
        return
    
    @dataclass
    class Fore:
        RED=''
        GREEN = ''

init(autoreset=True)
# Adding argparse
parser = ArgumentParser(prog='Hot-Reload',description='A simple program for running scripts when a file or specific files and a whole folder with execptions you provide',add_help=True, color=True)

parser.add_argument('cmd', help='The command to run when the file is changed', type=str)
parser.add_argument('-file', '-f', required=True, help='The file to watch for the change eg. "main.py"')
parser.add_argument('-ext', default='py', help='Accepted files to check for change eg. py or "py,json,toml"')
parser.add_argument('--folder', action='store_true',help='Watches the entire folder for change')

commands = parser.parse_args(sys.argv[1:])

cmd = commands.cmd
working_dir = Path(os.getcwd())

file_path = Path(working_dir / Path(commands.file))

# check if file exist
if not file_path.exists():
    print(f'{Fore.RED}{file_path} File do not exist')
    sys.exit(0)

use_folder = commands.folder

# add accepted execptions
accepted_ext = [f'*.{ext}' for ext in commands.ext.split(',')]


def get_change_time():
    if use_folder:
        lst = []
        for ext in accepted_ext:
            lst.extend(Path(working_dir).glob(ext))
        t = 0
        for file in lst:
            t+=os.path.getmtime(file)

        return t
    else:
        return os.path.getmtime(file_path)


running = False
print('\n')
prompt = lambda : print(f'{Fore.GREEN}HOTRELOAD: New Process Started\n')

while True:
    try:
        # create the start process
        if working_dir and not running:
            os.chdir(working_dir)
            last_change = get_change_time()
            prompt()
            run = subprocess.Popen(cmd)
        current_change = get_change_time()
        running = True
        
        # check if the file has changed 
        if last_change < current_change:
            run.terminate()
            run.kill()
            prompt()
            
            run = subprocess.Popen(cmd)
            last_change = current_change
        time.sleep(0.3)
    
    except KeyboardInterrupt:
        run.terminate()
        run.kill()
        break