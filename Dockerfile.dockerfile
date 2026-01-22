FROM python:3.9-slim
LABEL developer="Ayush Chaudhary"
LABEL qualification="B.Tech Information Technology"

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN chmod +x install.sh && ./install.sh

ENTRYPOINT ["phishdetect"]
CMD ["--help"]