# Adaptive Math AI

An AI-powered adaptive learning platform for mathematics education.

This project demonstrates how artificial intelligence can be combined with adaptive learning techniques to personalize math practice for students.

The platform dynamically adjusts exercises according to student performance, reinforces weak topics, and generates new variations of questions using a Large Language Model (LLM) hosted on Hugging Face.

---

# Features

## Student Adaptive Quiz

* Students answer math exercises in real time
* Questions adapt based on student performance
* Incorrect answers generate reinforcement questions
* Correct answers increase topic mastery
* Topics are removed only after sufficient reinforcement

---

## AI-Generated Question Variants

* Uses the `microsoft/Phi-3-mini-4k-instruct:featherless-ai` model
* Hosted remotely through Hugging Face Inference Providers
* Dynamically generates similar math problems
* Falls back to procedural Python generation if AI fails

---

## Reinforcement Learning Logic

* Weak topics stay longer in the active pool
* Mastered topics gradually disappear
* Students continue practicing until mastery threshold is reached

---

## FastAPI Backend

* Lightweight REST API
* Modular architecture
* Easy to extend

---

## Vue Frontend

* Simple student interface
* Loading states
* Adaptive question flow
* Prevents double submissions
* Disables empty submissions

---

# Tech Stack

## Frontend

* Vue 3
* Vite

## Backend

* Python
* FastAPI
* Uvicorn

## AI

* Hugging Face Inference Providers
* Microsoft Phi-3 Mini 4K Instruct

---

# Project Structure

```text
adaptive-math-ai/
│
├── backend/
│   ├── app/
│   │   ├── core/
│   │   │   └── config.py
│   │   │
│   │   ├── models/
│   │   │   └── schemas.py
│   │   │
│   │   ├── routes/
│   │   │   ├── exercises.py
│   │   │   ├── dashboard.py
│   │   │   └── student.py
│   │   │
│   │   ├── services/
│   │   │   ├── ai_service.py
│   │   │   ├── quiz_state.py
│   │   │   └── topic_definitions.py
│   │   │
│   │   └── main.py
│   │
│   ├── .env
│   ├── requirements.txt
│   ├── run.py
│   └── venv/
│
├── frontend/
│   ├── src/
│   │   ├── views/
│   │   │   └── StudentView.vue
│   │   │
│   │   ├── router/
│   │   └── main.js
│   │
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

# How the Adaptive System Works

The system maintains an internal pool of active questions.

---

# Initial State

The quiz starts with a predefined pool:

```python
[
  {
    "topic": "addition",
    "question": "5 + 5 = ?",
    "answer": "10"
  },
  {
    "topic": "subtraction",
    "question": "8 - 3 = ?",
    "answer": "5"
  }
]
```

---

# If Student Answers Correctly

* Topic mastery increases
* The current question is removed
* Once mastery threshold is reached:

  * The entire topic is removed from the pool

---

# If Student Answers Incorrectly

* Topic mastery decreases
* AI generates a new variation
* The new question is added to the active pool

Example:

```text
Original:
8 - 3 = ?

Generated:
14 - 9 = ?
```

This creates reinforcement learning behavior.

---

# AI Architecture

The project uses the following hosted model:

* `microsoft/Phi-3-mini-4k-instruct:featherless-ai`

through:

* Hugging Face Inference Providers

The backend sends prompts like:

```text
Generate 1 NEW math exercise.
Keep same learning objective.
Return ONLY valid JSON.
```

The AI responds with JSON:

```json
[
  {
    "question": "14 - 9 = ?",
    "answer": "5"
  }
]
```

---

# Environment Variables

The backend uses a `.env` file.

Create this file inside `/backend`:

```env
AI_API_URL=https://router.huggingface.co/v1/chat/completions

AI_API_KEY=your_huggingface_token_here

AI_MODEL=microsoft/Phi-3-mini-4k-instruct:featherless-ai

BACKEND_PORT=12000
```

---

# Installation Guide

## 1. Clone Repository

## 2. Create Hugging Face Account

Create a free account:

[Hugging Face](https://huggingface.co?utm_source=chatgpt.com)

---

## 3. Generate Hugging Face Access Token

Go to:

[Hugging Face Tokens Settings](https://huggingface.co/settings/tokens?utm_source=chatgpt.com)

Create a token with read permissions.

Copy the token into your `.env` file.

---

## 4. Setup Backend

Go to backend folder:

```bash
cd backend
```

Create virtual environment.

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 5. Start Backend

Run FastAPI server:

```bash
python run.py
```

Backend will run at:

```text
http://localhost:12000
```

---

## 6. Setup Frontend

Open another terminal.

Go to frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

---

## 7. Start Frontend

Run:

```bash
npm run dev
```

Frontend will run at:

```text
http://localhost:5173
```

---

# Running the Full System

You should now have:

| Service         | Port  |
| --------------- | ----- |
| FastAPI Backend | 12000 |
| Vue Frontend    | 5173  |

The AI model is hosted remotely on Hugging Face, so no local LLM installation is required.

---

# Example Workflow

1. Student opens quiz
2. System selects random question
3. Student submits answer
4. Backend evaluates correctness
5. AI generates reinforcement question if needed
6. Pool updates dynamically
7. Quiz continues until all topics are mastered

---

# Current MVP Limitations

This project was built for educational purposes as a proof of concept. Because the project uses a free hosted LLM:

* responses may occasionally be slow
* JSON formatting may fail
* generated questions may sometimes be repetitive
* small models may occasionally misunderstand prompts

The backend includes safeguards and fallback generation to maintain stability.
