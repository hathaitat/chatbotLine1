FROM python:3.7.3-stretch

WORKDIR /opt/app

RUN cd /opt/app


RUN pip3 install flask flask-restful waitress requests line-bot-sdk response

# RUN apt-get install unixodbc unixodbc-dev freetds-dev tdsodbc -y
# RUN pip3 install pyodbc == 4.0.26

# RUN git clone https://github.com/hathaitat/chatbotLine.git
RUN git clone https://hathaitat:hathaitat123456@github.com/hathaitat/chatbotLine.git

RUN cd /opt/app/chatbotLine

RUN export FLASK_APP=__main__.py
RUN export LC_ALL=C.UTF-8
RUN export LANG=C.UTF-8

ENTRYPOINT ["python3"]
CMD ["/opt/app/chatbotLine/server.py"]
EXPOSE 5000