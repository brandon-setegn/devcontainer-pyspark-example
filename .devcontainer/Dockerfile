
FROM jupyter/pyspark-notebook:python-3.10.4

# Install Curl
USER root
RUN apt update
RUN apt upgrade -y
RUN apt install -y curl
RUN wget -P /usr/local/spark-3.2.1-bin-hadoop3.2/jars/ https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-hadoop3-latest.jar

# Install Poetry
USER jovyan
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="$PATH:/home/jovyan/.poetry/bin"
# This will have poetry use the default installation of python and not create a new virtual env
RUN poetry config virtualenvs.create false

# Copy over spark configuration
COPY conf /usr/local/spark/conf
