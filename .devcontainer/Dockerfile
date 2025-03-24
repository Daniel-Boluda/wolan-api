FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV API_KEY="your_api_key"
ENV BROADCAST_ADDRESS="192.168.1.255"
ENV PORT=9

CMD ["python", "app.py"]
