# 🤖 AutoStream AI Assistant

An AI-powered conversational assistant that helps users explore pricing plans and captures leads for business use.

---

## 🚀 Features

* Intent Detection (Pricing, Plans, Buying Intent)
* Retrieval-based responses (RAG-style knowledge base)
* Multi-step Lead Capture (Name, Email, Platform)
* Tool Execution (Mock API for lead storage)
* Conversational flow with memory

---

## 🧠 How it works

1. User interacts with chatbot
2. System detects intent (pricing / buying)
3. Provides relevant responses from knowledge base
4. If user shows buying interest → starts lead capture
5. Collects:

   * Name
   * Email
   * Platform
6. Executes tool function to store lead

---

## 🛠️ Tech Stack

* Python
* CLI-based chatbot
* Basic NLP (intent detection using keywords)
* State management (lead flow)
* Mock API integration

---

## ▶️ How to Run

```bash
python app.py
```

---

## 💬 Example Interaction

```
You: I want to buy pro plan
Agent: What’s your name?
You: Aish
Agent: Email?
You: aish@gmail.com
Agent: Platform?
You: YouTube

Agent: Lead captured successfully!
```

---

## 🎯 Future Improvements

* Web UI (Flask)
* Database integration (SQLite / Google Sheets)
* LLM-based responses
* Better intent classification

---

## 👩‍💻 Author

Aishwarya Patil
