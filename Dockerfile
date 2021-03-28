FROM python:3.8-slim

WORKDIR /tmp
COPY requirements.txt /tmp
COPY app.log /tmp
COPY download_large_file_split.py /tmp
COPY unit_testing.py /tmp

RUN chmod +x download_large_file_split.py
RUN pip install -r requirements.txt

CMD [ "python", "./download_large_file_split.py"]
