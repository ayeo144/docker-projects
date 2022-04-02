# Docker Bind Mount tests

A small FastAPI (/code/app/app.py) application allowing a user to input 
some text which is written to a log file.

When run in a Docker container, the "log" file within the project
can bind to a folder outside the Docker container on the host machine. 
Then, any entries posted to the API will be written to the log file
in the volume on the host machine.

`docker run -d -p <host-port>:80 -v ~/output-from-container:/code/logs --name <container-name> <image>`