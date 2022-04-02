# Docker Bind Mounts and Volumes

A small FastAPI (/code/app/app.py) application allowing a user to input 
some text which is written to a log file.

## Bind Mounts

When run in a Docker container, the "log" file within the project
can bind to a folder outside the Docker container on the host machine. 
Then, any entries posted to the API will be written to the log file
in the volume on the host machine.

`docker run -d -p <host-port>:80 -v ~/bind-mount:/code/logs --name <container-name> <image>`

## Volumes

Create volume for storing logs from app...

`docker volume create <volume-name>`

Run the container using the volume instead of the bind mount. We mount the volume `aoi-logs` to the 
the folder `/code/logs` within the container.

`docker run -d -p <host-port>:80 --mount source=<volume-name>,target=/code/logs --name <container-name> <image>`

Then to later copy data from the volume to the host machine, we can use a dummy container...

`docker container create --name <container-name> -v <volume-name>:/root hello-world`

We can use the lightweight `hello-world` image for this. Finally copy from the dummy container to
the host machine...

`docker cp <container-name>:/root/ /some/folder/on/host/machine`

And to copy from the host to the container, just reverse the order of the source/destination in the above command.