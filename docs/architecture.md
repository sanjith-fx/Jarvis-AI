# 🏗️ Jarvis AI - System Architecture

## Overview

Jarvis AI follows a modular architecture where each module has a single responsibility. This design makes the project easier to maintain, debug, and extend as new features are added.

---

# High-Level Architecture

```
                    User
                     │
             🎤 Voice Command
                     │
                     ▼
          Speech Recognition
              (listen.py)
                     │
                     ▼
          Command Handler
       (command_handler.py)
                     │
        ┌────────────┴────────────┐
        │                         │
        ▼                         ▼
 Browser Automation          AI Engine
 (browser.py)              (brain.py)
        │                         │
        ▼                         ▼
   Chrome Browser          Ollama + Llama 3
        │                         │
        └────────────┬────────────┘
                     ▼
            Voice Response
              (speak.py)
                     │
                     ▼
                   User
```

---

# Project Structure

```
Jarvis-AI/

│
├── main.py
├── config.py
│
├── ai/
│   └── brain.py
│
├── browser/
│   └── browser.py
│
├── commands/
│   └── command_handler.py
│
├── voice/
│   ├── listen.py
│   └── speak.py
│
├── memory/
│   └── memory.py
│
└── data/
```

---

# Module Responsibilities

## main.py

Responsible for:

- Starting Jarvis
- Running the main loop
- Receiving user commands
- Passing commands to the Command Handler

---

## listen.py

Responsible for:

- Accessing the microphone
- Recording audio
- Converting speech into text

Technology:

- SpeechRecognition
- PyAudio

---

## speak.py

Responsible for:

- Converting text into speech
- Speaking responses to the user

Technology:

- pyttsx3

---

## command_handler.py

Responsible for:

- Processing commands
- Routing commands to the correct module
- Calling Browser functions
- Calling AI when necessary

This module acts as the brain that decides what Jarvis should do.

---

## browser.py

Responsible for:

- Opening websites
- Searching YouTube
- Browser automation
- Selenium interactions

Technology:

- Selenium
- ChromeDriver

---

## brain.py

Responsible for:

- Communicating with Ollama
- Sending prompts
- Receiving AI responses

Technology:

- Ollama
- Llama 3

---

## memory.py

Responsible for:

- Saving data
- Loading user memory
- Future long-term memory support

Current Storage:

- JSON

Future:

- SQLite
- Vector Database

---

# Current Command Flow

```
User

↓

"Open YouTube"

↓

listen.py

↓

command_handler.py

↓

browser.py

↓

Chrome Opens

↓

speak.py

↓

"Opening YouTube."
```

---

# AI Command Flow

```
User

↓

"What is Artificial Intelligence?"

↓

listen.py

↓

command_handler.py

↓

brain.py

↓

Ollama

↓

AI Response

↓

speak.py
```

---

# Design Principles

- Modular Architecture
- Single Responsibility Principle
- Scalable Design
- Offline First
- Easy Maintenance
- Future AI Expansion

---

# Future Architecture (Version 2)

The next version will introduce an Intent Router and Skill System.

```
                User
                  │
                  ▼
         Speech Recognition
                  │
                  ▼
          Intent Detection
                  │
                  ▼
          Command Router
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
 Browser      System       AI Skills
     │            │            │
     └────────────┼────────────┘
                  ▼
             Voice Response
```

This architecture will replace large if-else chains with a scalable skill-based system.