# AI Coding Agent

A CLI-based AI coding agent built with Python and Google Gemini, following the [Boot.dev](https://boot.dev) AI agents course. The agent operates in an agentic loop — planning, calling tools, observing results, and iterating — until it completes a task or hits a safety limit.

---

## What It Does

You give the agent a natural language prompt. It then autonomously:

1. Plans which tools to call
2. Executes those tools (read files, write files, run code, list directories)
3. Observes the results and decides what to do next
4. Repeats until the task is done

All file operations are **sandboxed** to the `./calculator` working directory.

---

## Key Concepts

This project is a hands-on exploration of how AI agents actually work under the hood:

| Concept | Where It Lives |
|---|---|
| **Agentic loop** — iterative LLM calls until task completion | `main.py` |
| **Tool/function calling** — LLM decides which tools to invoke | `functions/call_function.py` |
| **Tool schemas** — typed declarations that describe tools to the model | `functions/get_files_info.py`, etc. |
| **Conversation history** — appending messages to maintain context | `functions/generate_content.py` |
| **Sandboxing** — path validation to restrict file access | `functions/get_files_info.py`, `functions/get_file_content.py` |
| **Iteration limits** — guard against infinite loops | `config.py` (`MAX_AGENT_ITERATIONS = 20`) |

---

## Available Tools

The agent has access to four tools:

- **`get_files_info`** — list files and directories
- **`get_file_content`** — read file contents (with character limit)
- **`run_python_file`** — execute a Python file with optional arguments
- **`write_file`** — create or overwrite a file

---

## Setup

**Prerequisites:** Python 3.13+, [`uv`](https://docs.astral.sh/uv/)

```bash
# 1. Clone the repo
git clone <repo-url>
cd ai-agent

# 2. Install dependencies
uv sync

# 3. Add your Gemini API key
cp .env.example .env
# Edit .env and set GEMINI_API_KEY=your_key_here
```

Get a free Gemini API key at [aistudio.google.com](https://aistudio.google.com).

---

## Usage

```bash
# Basic usage
uv run main.py "fix the bug in calculator.py"

# Verbose mode (shows token counts and raw function responses)
uv run main.py "add a square root function" --verbose
```

The agent will print each tool it calls as it works, then output its final response.

---

## Project Structure

```
ai-agent/
├── main.py                  # Entry point, agent loop
├── config.py                # Constants (max iterations, working dir, etc.)
├── prompts.py               # System prompt
├── functions/
│   ├── generate_content.py  # Gemini API calls + response handling
│   ├── call_function.py     # Tool dispatcher + schema registry
│   ├── get_files_info.py    # Tool: list directory contents
│   ├── get_file_content.py  # Tool: read file contents
│   ├── run_python_file.py   # Tool: execute Python files
│   ├── write_file.py        # Tool: write/overwrite files
│   ├── args.py              # CLI argument parsing
│   └── env_or_throw.py      # Safe environment variable loading
└── calculator/              # Sandboxed working directory for the agent
```

---

## Configuration

| Variable | Default | Description |
|---|---|---|
| `MAX_AGENT_ITERATIONS` | `20` | Max tool-call cycles before forced exit |
| `MAX_CHARS` | `10000` | Max characters returned when reading a file |
| `WORKING_DIR` | `./calculator` | Sandboxed directory the agent can access |

---

## Customizing the Agent's Personality

The agent's personality and behavior are controlled entirely by the system prompt in [prompts.py](prompts.py).

### Current Personality: Blood Death Knight

Out of the box, your agent is a **menacing World of Warcraft Blood Death Knight** — a vampiric, undead warrior who serves the Ebon Blade and definitely has opinions about the Alliance.

> *"You are a menacing but helpful horde blood death knight AI coding agent. Lok'tar ogar! DEATH TO THE ALLIANCE!"*

Expect dramatic flair, Horde loyalty, and a surprising willingness to help you fix bugs. FOR THE HORDE.

---

### Changing the Personality

The system prompt does two things:

1. **Sets the tone** — how the agent talks and presents itself
2. **Defines what the agent knows it can do** — the list of available operations described in plain English

To change the personality, just edit `prompts.py`:

```python
system_prompt = """
You are a friendly and concise senior software engineer.

You help users with coding tasks by working through problems step by step.
You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory.
"""
```

> **Tip:** Keep the description of available operations accurate — the model uses this context to decide which tools to call and when.

---

## Model

Uses **Gemini 2.5 Flash** via the `google-genai` SDK.
