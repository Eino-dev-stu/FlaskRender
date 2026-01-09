FROM python:3.11-alpine
WORKDIR /usr/src/app

COPY data.html .

# No hardcoded ENV here—set REACT_APP_BACKEND_URL in Render dashboard
EXPOSE $PORT  
# Shell form to expand $PORT
CMD ["sh", "-c", "python -m http.server $PORT --bind 0.0.0.0"]