# Travel_planner

A lightweight multi-agent travel planning project built with AutoGen AgentChat.

## What it does

The project uses three agents to generate a complete travel plan:

- **Planner**: creates the itinerary structure (days, timing, flow)
- **Researcher**: finds food spots and recommendations
- **Writer**: turns the plan + research into a polished, readable itinerary

## Setup

1. Install dependencies
2. Configure model settings in `Travel_planner/config/settings.py` (API key, model name, optional termination word)

## Run

Run from the project root and execute the project entry script (for example `vacation_planner.py`) or start the team workflow from your notebook/script.

## Files

- `planner.py` — Planner agent (and shared model client)
- `researcher.py` — Researcher agent
- `writer.py` — Writer agent
- `teams.py` — Team wiring (group chat)
- `config/settings.py` — Configuration
