FROM python:3.11-alpine
WORKDIR /usr/src/app

COPY data.html .

ENV REACT_APP_BACKEND_URL=http://localhost:5000
EXPOSE 3000
# Start Python HTTP server
CMD ["python", "-m", "http.server", "3000", "--bind", "0.0.0.0"]