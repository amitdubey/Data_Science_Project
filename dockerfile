
FROM python:3.8-slim

COPY requirements.txt /tmp
COPY download_large_file_split.py /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt

CMD [ "python", "./download_large_file_split.py"]

