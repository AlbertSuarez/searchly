FROM python:3.7
ADD . /srv/searchly
WORKDIR /srv/searchly
RUN pip install --upgrade pip
RUN pip3 install -r requirements.lock
RUN python3 -m nltk.downloader stopwords
CMD uwsgi --ini src/searchly.ini