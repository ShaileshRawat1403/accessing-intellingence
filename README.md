# 🎧 Spotify Song Recommendation Agent

A lightweight, LLM-powered agent that recommends songs based on your favorite artists using LangChain Runnables and Groq/OpenAI models. Tracks all executions via AgentOps for observability and debugging.

---

## 🚀 Project Overview

This project uses a modern **Runnable-based LLM chain** architecture with:

- 🔗 **LangChain** for building the agent
- 💬 **Groq** (LLaMA3) or **OpenAI GPT-3.5** as the LLM backend
- 🧠 **AgentOps** for session tracing and observability
- ✅ Clean `.env` based configuration

---

## 🧠 Use Case

> Input: `"I like the following artists: Drake, Future. Can I get 5 song recommendations?"`  
> Output: A curated list of 5 similar tracks based on style, genre, and artist vibe.

This agent is perfect for:
- Music discovery apps
- LLM-powered content experiences
- API chaining and enrichment pipelines
- Learning LangChain Runnable architecture

---

## 📁 Project Structure

```

spotify-agent/
├── .env
├── main.py                  # Entry point script
├── agent\_config.py          # LLM chain setup (Runnable)
├── tools.py                 # Custom logic (future tools)
└── README.md                # You're here

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

<sub>If `requirements.txt` is missing, install manually:</sub>

```bash
pip install langchain langchain-openai langchain-groq python-dotenv agentops
```

### 3. Configure `.env`

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your-openai-key-here
GROQ_API_KEY=your-groq-key-here
AGENT_OPS_KEY=your-agentops-key-here
```

> ✅ Only one of `OPENAI_API_KEY` or `GROQ_API_KEY` will be used based on how `agent_config.py` is written.

---

## ▶️ Running the Agent

```bash
python main.py
```

This will:

* Start an AgentOps trace session
* Run the prompt chain
* Return 5 song recommendations based on your input
* End the trace session (correctly, without crashes)

---

## 🧪 Example Output

```
🎵 Final Song Recommendations:

1. Travis Scott - Antidote
2. Young Thug - Pick Up the Phone
3. The Weeknd - The Hills
4. Migos - Bad and Boujee
5. Gunna - Sold Out Dates
```

---

## 📊 AgentOps Integration

* ✅ Full traceability
* ✅ Session replay links printed in terminal
* ✅ Crash visibility + metrics
* Future add-ons: custom tags, metrics logging

---

## 📌 Key Features

| Feature                  | Supported |
| ------------------------ | --------- |
| LangChain Runnable       | ✅         |
| LLM Choice (OpenAI/Groq) | ✅         |
| AgentOps tracing         | ✅         |
| Clean prompt chaining    | ✅         |
| Tool extension support   | 🔜        |
| Spotify API connection   | 🔜        |
| Web UI / Streamlit       | 🔜        |

---

## 📦 To Do Next

* [ ] Add Spotify Web API for track preview links
* [ ] Build a minimal Streamlit or Gradio frontend
* [ ] Add genre, mood, and decade filters
* [ ] Dockerize for deployment
* [ ] Unit tests with `pytest`

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss.

---

## 📄 License

MIT © 2025 Shailesh Rawat

```

---

Let me know if you want to:

- Push this to GitHub via terminal
- Generate `requirements.txt`
- Add badges (Python version, LangChain, Groq, etc.)

Shall I also scaffold a `docs/` folder or auto-create the Git commit and push steps?

