FROM terrillo/python3flask:latest

ENV STATIC_URL /static
ENV STATIC_PATH /webapp/static

# Place your flask application on the server
COPY ./webapp /webapp
WORKDIR /webapp

# Install requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python"]

# Start Server
CMD ["main.py"]

