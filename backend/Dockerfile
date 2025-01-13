FROM python:3.12.8

# Set the working directory
WORKDIR /app

# Copy application code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Start the application
CMD uvicorn app.main:app --host 0.0.0.0 --port 8000