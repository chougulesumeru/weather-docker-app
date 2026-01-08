#step 1: - use small pythin base image
FROM python:3.9-alpine

#step 2:- set a directory where all commands will run 
WORKDIR /code

#copy requirments form requirements.txt 
COPY requirements.txt .

#step 4:- run and install the requirements.txt 
RUN pip install -r requirements.txt 

#step 5:- copy the rest of application code
COPY . .

#step 6:- command to run the application
CMD ["python","app.py"]
