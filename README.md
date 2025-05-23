# Multi-Agent AI Assistant with Gemini-2.0

This project demonstrates how to create a multi-agent AI assistant system using the Gemini-2.0 model with Python. It uses different specialized agents to handle queries related to web development, mobile apps, DevOps, OpenAI SDK, and Agentic AI, and routes questions accordingly.

---

## Features

- Multiple AI agents with distinct roles and instructions:
  - Web Assistant
  - Mobile Assistant
  - OpenAI SDK Assistant
  - DevOps Assistant
  - Agentic AI Assistant (can use DevOps and OpenAI tools)
  - General Panacloud Assistant (routes queries to other agents)
- Uses Google's Gemini-2.0 language model (`gemini-2.0-flash`)
- Async programming with Python's `asyncio` for efficient task handling
- Environment variables support via `.env` for API keys
- Verbose logging enabled for debugging

---

## Setup Instructions

1. Clone this repository:

   ```bash
   git clone https://github.com/MubashirSaeed942/multi_agents_system
   cd multi_agents_system/src/app
   run script in terminal <python main1.py> or using UV <uv run main1.py>
