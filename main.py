import os
import sys
import subprocess

file = sys.argv[1]



path = os.getcwd()

running = False
while True:
    try:
        if path and not running:
            os.chdir(path)
            last_change = os.path.getmtime(file)
            run = subprocess.Popen(str(f'py {file}').split())
        current_change = os.path.getmtime(file)
        running = True
        
        
        if last_change < current_change:
            run.terminate()
            run.kill()
            prompt = 'New Process Started'
            print(f'{prompt:>10}')
            
            run = subprocess.Popen(str(f'py {file}').split())
            last_change = current_change
    except KeyboardInterrupt:
        run.terminate()
        run.kill()
        break