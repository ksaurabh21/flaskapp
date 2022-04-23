FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN python3 -m pip install --upgrade pip
RUN pip3 install flask
COPY . /opt/
CMD FLASK_APP=/opt/app.py flask run --host=0.0.0.0
#RUN cd /opt
#CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]