# 🎧 Spotify Song Recommendation Agent

A lightweight, LLM-powered agent that recommends songs based on your favorite artists using LangChain Runnables and Groq/OpenAI models. Tracks all executions via AgentOps for observability and debugging.

> Built to demonstrate how **modern LLM chains**, observability, and lightweight agents can plug into real-world tasks. This repo is not just code — it's a **teachable, extensible blueprint**.

---

## 🚀 Project Overview

This project showcases a modern **Runnable-based LLM chain** architecture with:

- 🔗 **LangChain** for building the agent and toolchain
- 💬 **Groq (LLaMA3)** or **OpenAI GPT-3.5** as the LLM backend
- 🧠 **AgentOps** for session tracing, observability, and replays
- ✅ Clean, `.env`-driven configuration
- 🧰 Ready for plug-and-play use or expansion into a full-stack app

---

## 🧠 Use Case

> **Prompt**: `"I like the following artists: Drake, Future. Can I get 5 song recommendations?"`  
> **Response**: A curated list of similar tracks based on genre, energy, and artist vibe.

This agent is ideal for:

- Music discovery apps
- LLM-powered recommendation engines
- Prompt chaining and enrichment pipelines
- Hands-on learning with LangChain Runnables + API integration

---

## 📁 Project Structure

```

spotify-agent/
├── .env                    # Environment keys (excluded from version control)
├── main.py                # Entry point script
├── agent\_config.py        # LLM agent + Runnable chain setup
├── tools.py               # Placeholder for extending functionality
└── README.md              # You're here

````

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/spotify-agent.git
cd spotify-agent
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

<sub>or install manually if `requirements.txt` is missing:</sub>

```bash
pip install langchain langchain-openai langchain-groq python-dotenv agentops
```

### 3. Configure Environment Keys

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your-openai-key-here
GROQ_API_KEY=your-groq-key-here
AGENT_OPS_KEY=your-agentops-key-here
```

> ✅ Only one LLM key is required — the agent will prioritize Groq by default if present.

---

## ▶️ Running the Agent

Run the agent with:

```bash
python main.py
```

Expected flow:

* Loads the environment keys
* Initializes the agent with tools and tracing
* Prompts user input for favorite artists
* Returns 5 song recommendations
* Prints AgentOps session replay link for debugging

---

## 🧪 Sample Output

```
🎵 Final Song Recommendations:

1. Travis Scott - "Sicko Mode"
2. Young Thug - "Pick Up the Phone"
3. The Weeknd - "The Hills"
4. Gunna - "Sold Out Dates"
5. Nav - "Wanted You"
```

> Traces are logged to AgentOps with replayable session links for every execution.

---

## 📊 AgentOps Observability

This project is instrumented with [AgentOps](https://www.agentops.ai/) to provide:

| Capability           | Status |
| -------------------- | ------ |
| Session Replay       | ✅      |
| Crash Tracing        | ✅      |
| Metrics + Logs       | ✅      |
| Future Custom Events | 🔜     |

> AgentOps helps you debug agents **as they behave**, not just at crash time.

---

## 📌 Key Features

| Feature                     | Status |
| --------------------------- | ------ |
| LangChain Runnable support  | ✅      |
| LLM switch (Groq/OpenAI)    | ✅      |
| AgentOps instrumentation    | ✅      |
| Clean prompt chaining       | ✅      |
| `.env`-based setup          | ✅      |
| Spotify Web API integration | 🔜     |
| Tool Extension Architecture | 🔜     |
| Frontend / UI (Streamlit)   | 🔜     |

---

## 📦 What's Next

* [ ] Integrate Spotify Web API for real-time track links
* [ ] Add genre/mood/decade filters
* [ ] Streamlit frontend for live demos
* [ ] Dockerize the setup for deployment
* [ ] Add logging & error handling hooks
* [ ] Unit test coverage with `pytest`

---

## 🎯 How This Helps You Learn

This repo is designed to help you:

* Understand how LangChain Runnables work (vs older Agents)
* Observe and debug LLMs via AgentOps
* Prototype LLM-powered use cases without bloated setups
* Expand into real-world integrations using Spotify, Groq, OpenAI, or your own tools

If you're new to agent-based systems or LLM chains, this project gives you **just enough to learn and launch**.

---

## 🤝 Contributing

Pull requests are welcome. Please open an issue for discussion before large changes.

---

## 📄 License

MIT © 2025 Shailesh Rawat

---


