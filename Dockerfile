FROM rasa/rasa:3.6.18-full

# Copy project files into the container
COPY . /app

# Install extra dependencies if needed
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose port used by Rasa
EXPOSE 8080

# Run Rasa server
CMD ["rasa", "run", "--enable-api", "--cors", "*", "--port", "8080"]
