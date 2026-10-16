# Lab 01: Python Web Application Using Docker

## Objective

Build and run a simple Python web application inside a Docker container and access it through a web browser.

## Technologies

- Linux (Ubuntu on WSL)
- Docker
- Python 3
- Git and GitHub
- HTTP

## Project Structure

```text
lab-01/
├── README.md
├── Dockerfile
└── app.py
```

## Architecture

Browser → Host Port 8000 → Docker Container Port 8000 → Python HTTP Server

## Implementation Steps

### 1. Build the Docker image

From this directory, run:

```bash
docker build -t madhu-docker-web:v1 .
```

### 2. Run the container

```bash
docker run -d --name madhu-web -p 8000:8000 madhu-docker-web:v1
```

### 3. Verify the running container

```bash
docker ps
```

### 4. Test the HTTP response

```bash
curl http://localhost:8000
```

Alternatively, open `http://localhost:8000` in a browser.

### 5. Inspect container logs

```bash
docker logs madhu-web
```

### 6. Stop and remove the container

```bash
docker rm -f madhu-web
```

## Key Learnings

- Created a Docker image using a Dockerfile.
- Ran a container from a custom image.
- Mapped a host port to a container port.
- Verified application availability using curl and a browser.
- Inspected container status and logs.

## Result

The Python web application ran successfully inside Docker and returned an HTML response through port 8000.

## Future Improvements

- Add Docker Compose.
- Publish the image to Docker Hub.
- Add automated build and test steps using CI/CD.
- Improve container security and health checks.
