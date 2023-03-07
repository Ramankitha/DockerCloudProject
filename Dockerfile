FROM python:3.8-alpine
WORKDIR /home/data1
COPY ./ ./
CMD ["python" ,"DockerCloud.py"]
