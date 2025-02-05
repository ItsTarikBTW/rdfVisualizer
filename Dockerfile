FROM python:3.12

# Install Graphviz system dependencies required by pygraphviz
RUN apt-get update && apt-get install -y graphviz libgraphviz-dev pkg-config

WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY . .

# Run the application
CMD ["python", "main.py"]