FROM python:3.11-alpine
WORKDIR /usr/src/app
# Install envsubst (for placeholder replacement)
RUN apk add --no-cache gettext
COPY data.html .
RUN envsubst < data.html > data.html.tmp && mv data.html.tmp data.html
# No hardcoded ENV here—set REACT_APP_BACKEND_URL in Render dashboard
EXPOSE $PORT  
# Shell form to expand $PORT
CMD ["sh", "-c", "python -m http.server $PORT --bind 0.0.0.0"]