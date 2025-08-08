FROM python:3.13.5-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY Vishva.py Vishva.py
COPY Vishva.txt Vishva.txt
RUN pip install flask
EXPOSE 5000
CMD ["python3", "Vishva.py"]

