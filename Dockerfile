FROM python:3.11

WORKDIR /code

RUN apt-get update && apt-get install -y libgomp1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# move the static production React UI into the build subdirectory
COPY ui/build/ build/

EXPOSE 3000


CMD ["gunicorn", "-b", ":3000", "app:app"]

