
# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

# this creates the working directory inside our container
WORKDIR code/

# copy the API code into the working directory
COPY . /code/

# install the requirements
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# run the API
CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "5000"]