FROM python:3.6

RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="VIRTUAL_ENV/bin:$PATH"

WORKDIR /app
COPY requirements.txt .
# Install dependencies
RUN pip install -r requirements.txt
COPY . .


CMD ["python", "run.py"]
