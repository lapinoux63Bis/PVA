FROM ubuntu

RUN apt update -y && apt install python3 -y

WORKDIR /root

COPY Receiver.py .

EXPOSE 12345/udp
EXPOSE 12346/udp

CMD [ "python3", "Receiver.py" ]
