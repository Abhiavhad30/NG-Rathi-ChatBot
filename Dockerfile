FROM rasa/rasa:3.6.18-full

# Work directory
WORKDIR /app

# Copy project files
COPY . .

# Fix: prevent setuptools uninstall permission error
RUN pip install --upgrade --ignore-installed setuptools==65.7.0

# Install requirements
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["rasa", "run", "--enable-api", "--cors", "*", "--port", "8080"]
