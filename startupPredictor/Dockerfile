# Use an official Python runtime as a parent image
FROM python:3.11.0

# setup environment variable  
ENV DockerHOME=/startupPredictor

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=True

# copy whole project to your docker home directory. 
COPY . $DockerHOME  

# run this command to install all dependencies  
COPY requirements.txt $DockerHOME  
RUN pip install -r requirements.txt  

# port where the Django app runs  
EXPOSE 8000  

# start server  
CMD ["python", "manage.py", "runserver"] 
