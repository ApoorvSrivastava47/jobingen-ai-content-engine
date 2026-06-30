# 🚀 JobInGen AI Engine

> A modular Multi-Agent AI Content Generation System built for scalable, high-quality content creation.

---

## 📖 Overview

JobInGen AI Engine is an AI-powered backend designed around a **Multi-Agent Architecture**.

Instead of asking a single LLM to generate content directly, the system separates the complete workflow into specialized AI agents.

Each agent performs one responsibility:

- Plan the content
- Generate the draft
- Review the quality
- Decide whether regeneration is required

This architecture makes the system:

- Modular
- Maintainable
- Easy to extend
- Provider independent (Ollama, Gemini, OpenAI)

---

# ✨ Features

- 🤖 Multi-Agent Architecture
- 🧠 Planner Agent
- ✍️ Copywriter Agent
- 🔍 Critic Agent
- 🔄 Automatic Rewrite Loop
- 📝 Prompt Engineering Pipeline
- 🎭 Persona-based Prompt Loading
- 🏗 Modular AI Provider Layer
- ⚙️ Configuration Driven
- 🔌 Easy LLM Provider Switching
- 📂 Clean Project Structure

---

# 🏗 System Architecture

```
                    User
                      │
                      ▼
              Content Workflow
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
    Planner      Copywriter      Critic
        │             │             │
        └─────────────┼─────────────┘
                      ▼
               Review Parser
                      │
             Rewrite Required?
               │            │
               ▼            ▼
          Publish      Rewrite Draft
```

---

# 🤖 AI Agents

## 🧠 Planner Agent

Responsible for planning the content strategy.

Outputs:

- Topic
- Goal
- Tone
- Content Pillar
- Template

---

## ✍️ Copywriter Agent

Generates high-quality content using:

- Persona
- Context
- Instructions

---

## 🔍 Critic Agent

Evaluates generated content.

Checks:

- Brand Voice
- Hook
- Value
- CTA
- Grammar
- Formatting

---

## 🔄 Review Parser

Reads critic feedback.

Decides:

- Publish
- Rewrite

without exposing that logic to the workflow.

---

# ⚙ Workflow

```
User Topic

↓

Planner

↓

Strategy

↓

Copywriter

↓

Content

↓

Critic

↓

Review Parser

↓

Publish
or
Rewrite
```

---

# 🏛 Human Analogy

| Software Component | Human Equivalent |
|--------------------|------------------|
| ContentWorkflow | Project Manager |
| PlannerAgent | Strategic Planner |
| Copywriter | Professional Content Writer |
| Critic | Quality Auditor |
| ReviewParser | Decision Officer |
| AIService | Receptionist |
| AIClientFactory | HR Department |
| PersonaLoader | Company Library |
| PromptBuilder | Document Composer |









---

# 📂 Project Structure

```text
backend/
│
├── app/
│   ├── agents/
│   ├── clients/
│   ├── config/
│   ├── core/
│   ├── critic/
│   ├── persona/
│   ├── prompt_builder/
│   ├── utils/
│   ├── workflow/
│   └── tests/
│
├── prompts/
├── outputs/
├── logs/
├── data/
└── .env
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/ApoorvSrivastava47/jobingen-ai-content-engine.git
```

Move into the backend

```bash
cd backend
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start Ollama

```bash
ollama serve
```

Pull the model

```bash
ollama pull llama3.2
```

Run the workflow

```bash
python -m app.tests.test_planner
```

---

# ▶ Example Workflow

```
Topic

↓

Planner

↓

Strategy

↓

Copywriter

↓

Draft

↓

Critic

↓

Review

↓

Review Parser

↓

Publish
or
Rewrite
```

---

# 💻 Tech Stack

- Python
- Ollama
- LLM Provider (Currently Ollama + Llama 3.2)
- Loguru
- PyYAML
- Markdown
- Git
- Object-Oriented Programming
- Prompt Engineering

---

# 🎯 Why Multi-Agent?

Instead of relying on a single prompt, the system separates planning,
content generation,
quality evaluation,
and orchestration into independent AI agents.

Benefits:

- Better maintainability
- Easier debugging
- Reusable agents
- Model independence
- Cleaner architecture

---

# 🚀 Future Scope

- OpenAI Integration
- Gemini Integration
- Claude Integration
- Streaming Responses
- FastAPI Backend
- React Frontend
- Docker Deployment
- Authentication
- Analytics Dashboard
- Human Feedback Loop
- Multi-language Content Generation

---

# 👨‍💻 Author

**Apoorv Srivastava**

AI & ML Engineer

GitHub:
https://github.com/ApoorvSrivastava47

---

# ⭐ Acknowledgements

Developed as part of the JobInGen AI Content Engine Hackathon.

Built using a modular Multi-Agent AI architecture with provider-independent design.