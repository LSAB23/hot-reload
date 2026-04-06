A simple program for running scripts when a file or specific files and a whole folder with execptions you provide

positional arguments:
  cmd             The command to run when the file is changed

options:
  -h, --help      show this help message and exit
  -file, -f FILE  The file to watch for the change eg. "main.py"
  -ext EXT        Accepted files to check for change eg. py or
                  "py,json,toml"
  --folder        Watches the entire folder for change