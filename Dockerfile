FROM python:3@sha256:11560799e4311fd5abcca7ace13585756d7222ce5471162cd78c78a4ecaf62bd

ADD requirements.txt /

RUN pip install -r requirements.txt

ADD api.py cli.py /

ENTRYPOINT [ "python", "./cli.py", "--mac-address" ]
