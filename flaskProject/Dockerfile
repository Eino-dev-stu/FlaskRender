FROM python:3.11-alpine

WORKDIR /usr/src/app


RUN pip install flask requests  flask-cors  pycountry 
RUN apk add --no-cache gcc musl-dev

COPY hello.py .
EXPOSE $PORT

# No hardcoded ENV here—set REQUEST_ORIGIN in Render dashboard
# Shell form to expand $PORT (assumes hello.py runs the server)
CMD ["sh", "-c", "python -u hello.py"]
