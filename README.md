# @clappingseal Telegram Bot Template

My template, use it if you like it. Inspired by mason's template, which I used for like 2 years.

## Features

- Aiogram
- FastStream
- Taskiq
- SQLAlchemy
- Dishka

## Infrastructure

The project is configured to work with Docker Compose but uses external infrastructure in the project's network. It requires PostgreSQL, Redis and RabbitMQ.

## Project Structure

Kinda hexagonal, idk? Pretty useful and scalable for Telegram bots. Most of my bots don't require more.

## Installation and Running

1. Clone
2. Install
3. Run infrastructure, configure environments for it
4. Run using Docker Compose:
```bash
docker-compose up -d
```
or on-device:
```bash
poetry run python -m src.app
```

## License

MIT
