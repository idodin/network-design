FROM python:3.7-slim-buster

WORKDIR /mnt/
COPY dispatcher /mnt/
COPY graphs /mnt/
COPY parsing /mnt/
COPY main.py /mnt/

CMD ["sh", "-c", "python main.py --input ${input} --output ${output} ${command} ${goal}"]