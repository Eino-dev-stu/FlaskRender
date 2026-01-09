FROM python:3.11-alpine

WORKDIR /usr/src/app


RUN pip install flask requests  flask-cors  pycountry 
RUN apk add --no-cache gcc musl-dev

COPY hello.py .
EXPOSE 5000
ENV REQUEST_ORIGIN=http://localhost:3000
CMD [ "python","-u", "hello.py" ]
