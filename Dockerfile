FROM python

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --upgrade pip \
  && pip install pylint \
  && pip install pytest

COPY . /app

RUN pylint src/factorial
	
RUN	pytest
