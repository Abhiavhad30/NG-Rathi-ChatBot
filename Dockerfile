FROM rasa/rasa:3.6.18-full

WORKDIR /app

COPY . .

# Fix for setuptools permission issue on Render
RUN pip install --ignore-installed setuptools==65.7.0

# Upgrade pip safely
RUN pip install --no-cache-dir --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["rasa", "run", "--enable-api", "--cors", "*", "--port", "8080"]
