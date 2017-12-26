FROM python:3.5  
ENV PYTHONUNBUFFERED 1  
RUN mkdir /config
ADD /config/requirements/dev.pip /config/
RUN pip install -r /config/dev.pip  
RUN mkdir /src;  
WORKDIR /src  