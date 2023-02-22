FROM python:3.7-stretch

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1

ENV HF_ENDPOINT // private repo
ENV MODEL_NAME bert-base-cased
ENV REVISION_ID a8d257ba9925ef39f3036bfc338acf5283c512d9

COPY ./src /src

WORKDIR /src

RUN pip install --disable-pip-version-check --no-cache-dir --upgrade -r ./requirements.txt

EXPOSE 8555

CMD ["python", "main.py"]