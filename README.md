# Redis Producer-Consumer Example with FastAPI

🚀 A simple implementation of the Producer-Consumer pattern using Redis and FastAPI.

This repository demonstrates how to build asynchronous communication between services using Redis as a message broker.

---

## 🔧 Technologies

- **FastAPI**: A modern, fast web framework for building APIs with Python.
- **Redis**: A powerful in-memory data structure store, used as a message broker.
- **aioredis**: An asynchronous Redis client library for Python.

---

## 📜 Features

### Producer:
- Publishes messages to a Redis channel using the `PUBLISH` command.
- Supports custom data submission through an API.

### Consumer:
- Subscribes to a Redis channel using the `SUBSCRIBE` command.
- Processes incoming messages asynchronously.

---

## 📂 Project Structure

- `producer/` — Producer implementation that publishes data to Redis channels.
- `consumer/` — Consumer implementation that subscribes to Redis channels and processes messages.
- `docker-compose.yml` — A quick setup for Redis using Docker.
- `README.md` — Detailed project documentation with usage examples.

---

## 🚀 How to Run?

1. Make sure Docker and Docker Compose are installed.
2. Start Redis via Docker:
   
   ```bash
   docker-compose up --build
