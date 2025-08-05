import os
import sys
import subprocess
import time
from pathlib import Path


file = sys.argv[1]

use_folder = False
if len(sys.argv) >=3:
    if sys.argv[2] == 'f':
        use_folder = True
path = os.getcwd()

running = False
prompt = 'New Process Started'

accepted_ext = ['*.py']

def get_change_time():
    if use_folder:
        lst = []
        for ext in accepted_ext:
            lst.extend(Path(path).glob(ext))
        t = 0
        for _ in lst:
            t+=os.path.getmtime(_)

        return t
    else:
        return os.path.getmtime(file)




while True:
    try:
        if path and not running:
            os.chdir(path)
            last_change = get_change_time()
            print(f'{prompt:<10}')
            run = subprocess.Popen(str(f'py {file}').split())
        current_change = get_change_time()
        running = True
        
        if last_change < current_change:
            run.terminate()
            run.kill()
            print(f'{prompt:<10}')
            
            run = subprocess.Popen(str(f'py {file}').split())
            last_change = current_change
        time.sleep(0.3)
    except KeyboardInterrupt:
        run.terminate()
        run.kill()
        break