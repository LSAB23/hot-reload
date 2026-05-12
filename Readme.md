usage: Hot-Reload [-h] -file FILE [-ext EXT] [--folder] cmd

A simple program for running scripts when a file or specific files
and a whole folder with execptions you provide eg. horeload
"command" -f="the file to watch" -ext="extensions,py,json,toml" and
--folder if it should watch the entire folder

positional arguments:
  cmd             The command to run when the file is changed

options:
  -h, --help      show this help message and exit
  -file, -f FILE  The file to watch for the change eg. "main.py"
  -ext EXT        Accepted files to check for change eg. py or
                  "py,json,toml"
  --folder        Watches the entire folder for change