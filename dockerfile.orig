# Defines the base image your container will use - in this case, the standard Python 3.12 image from the Docker Hub repository, which runs on a stripped-down verison of Linux that contains both Python and pip.
FROM python:3.12 

# Runs a command in the target operating system. In this case, it creates the directory /user/src/app, where we’ll stage our code.
RUN mkdir /usr/src/app

# Copies Python application, requirements.txt and data.json files to the application folder in the container image.
COPY s3.py /usr/src/app
COPY requirements.txt /usr/src/app
COPY data.json /usr/src/app

# Switches the current working directory to our app folder.
WORKDIR /usr/src/app

# Here, the RUN command uses pip to install all the Python libraries your app will need.
RUN pip install -r requirements.txt

# Specifies the command that your container will run on startup. In other words, when your container starts running, it’ll run your Python application to perform your data transformation workload.
CMD ["python", "./s3.py"]
