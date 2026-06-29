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
