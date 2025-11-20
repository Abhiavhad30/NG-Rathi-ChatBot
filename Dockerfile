FROM rasa/rasa:3.6.18-full

WORKDIR /app

COPY . .


# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["rasa", "run", "--enable-api", "--cors", "*", "--port", "8080"]
