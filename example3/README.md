# Dockerize a Python web app

## 1. Create the app locally 

```console
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install fastapi uvicorn
```

Try it:

```console
$ uvicorn app.main:app --port 80
```

Save dependencies:

```console
$ pip freeze > requirements.txt
```

## 2. Build the Docker image

```console
$ docker build -t fastapi-image-dvd . 
```

Note that we use a `.dockerignore` file to ignore certain files/folders.

## 3. Run the Docker image

Normal:

```console
$ docker run -p 80:80 fastapi-image-dvd
```

Run in background and give a name:

```console
$ docker run -d --name fastapi-image-dvd -p 80:80 fastapi-image
```

`-p 80:80`: Map the port from outside to the port from the container

Host in Dockerfile must be:

`host: 0.0.0.0`: "placeholder", it tells a server to listen for and accept connections from any IP address ("all IPv4 addresses on the local machine").

## 4. Run your container as Workspace Develpment: 
In this way your source-codes files will be relationed by docker a volume in your local computer directory (HOST) to the CONTAINER:
```console
$ docker run -p 8000:8000 -v ${pwd}:/opt/app/src --name fastapi-container-dvd -d fastapi-workspace-dvd
```
Now the './src' directory in docker container will be sincronyzed with local files, where possible you have a git repository
Ensure that is running the command above in directory related as ${PWD}

## 5. Install a Docker Plugin on VSCode, from Microsoft. 

On VSCode left menu Docker icon >> containers >> right click on fastapi-container-dvd >> click on 'Attach Visual Studio' Code, or use SRC LOCAL to EDIT

Now you will be able to operarate your VSCode inner the container, press CTRL + ' to open terminal, and observe that you will be in the container file directory.

On stop container your /src/* files will be in 
