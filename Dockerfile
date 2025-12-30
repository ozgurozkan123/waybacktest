FROM python:3.11-slim

# Install system dependencies and Go toolchain to build waybackurls
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    ca-certificates \
    build-essential \
    golang \
  && rm -rf /var/lib/apt/lists/*

# Install waybackurls (tomnomnom)
ENV GOPATH=/root/go
ENV PATH="$GOPATH/bin:/usr/local/go/bin:$PATH"
RUN go install github.com/tomnomnom/waybackurls@latest

WORKDIR /app

# Copy requirements first for layer caching
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

ENV HOST=0.0.0.0
EXPOSE 8000

CMD ["python", "server.py"]
