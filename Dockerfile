# first layer is our python base image enabling us to run pip
FROM python:3.9.6

# create directory in the container for adding your files
WORKDIR C:\projects\robot_challenge

# copy over the requirements file and run pip install to install the packages into your container at the directory defined above
COPY requirements.txt ./ 
RUN pip install --no-cache-dir -r requirements.txt --user 
COPY . . 


# enter entry point parameters executing the container
ENTRYPOINT ["python", "./test.py"]
