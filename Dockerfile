FROM python:3.8-alpine
WORKDIR /home/data
COPY ./ ./
CMD ["python" ,"DockerCloud.py"]