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


## The author's disclaimer, bullshit and stream of thought and why did he put THIS in public access anyway (inspiration ✨ ahh paragraph 🥀)

Guys, I'm stuck in the capitalist wheel of assembling bots for businesses of different sizes. I can't say that I don't like it. I'm making this template mostly for myself, but if you liked it - feel free to use it. Now a real disclaimer: the architecture is cool, but it is far from ideal here, but at the moment the structure of this project covers 100% of all requests from businesses looking for solutions to their problems on a freelance basis. I also write a backend for startups and generally love architectural discussions in chats, but as a solo developer, I DAMN don't have that much time to practice THE best and most reliable practices for deploying on 800 servers in different data centers, this is DEFINITELY not for telegram bots and startups. Because ... (reread the first sentence). And I am ready to defend this position and this template proudly hangs publicly in my account, manifesting my point of view. I apologize for the pathos, since I can definitely be wrong in the implementation of any of the technologies used in this template due to lack of REAL 💪 highload and enterprise experience and I will be glad to hear your criticism and suggestions. The approach described in this template was enough for me to implement both fairly loaded bots and bots with complex, intricate logic (where it was NECESSARY to use aiogram-dialog, here it is cut out because in most cases it is a fierce overkill). With this approach, when the load increases or the project expands, there is always enough vertical scaling. Bots that require more can be counted on the fingers, and businesses that have such requests do not turn to freelancers who are looking for convenient templates, which is what this repository is. This template provides a good balance for you as a developer between the pleasure of sniffing your own farts and assembling the most abstract models and interfaces possible on dataclasses, and the time you spend assembling a solution for a business that came to you as a freelancer, for which they are willing to wait and pay for it. Prove me wrong.
Enjoy using it.