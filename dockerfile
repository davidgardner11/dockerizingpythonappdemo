# Defines the base image your container will use - in this case, a docker image containing both Python 3.12 and Prefect libraries pre-installed, running on a stripped-down verison of Linux
FROM prefecthq/prefect:2-python3.12-conda

# Runs a command in the target operating system. In this case, it creates the directory /user/src/app, where we’ll stage our code.
RUN mkdir /usr/src/app

# Copies Python application and requirements.txt files to the application folder in the container image.
COPY s3-flow.py /usr/src/app
COPY requirements.txt /usr/src/app

# Switches the current working directory to our app folder.
WORKDIR /usr/src/app

# Here, the RUN command uses pip to install all the Python libraries your app will need.
RUN pip install -r requirements.txt

# Specifies the command that your container will run on startup. In other words, when your container starts running, it’ll run your Python application to perform your data transformation workload.
CMD ["python", "s3-flow.py"]
