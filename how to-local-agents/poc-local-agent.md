
# POC: Create Your First Local AI Agent

This guide walks you through a **proof of concept (POC)** for creating a simple AI agent on your local machine.  
It’s written so even **beginners** can follow along, while still being useful for DevOps engineers.

---

## 🌟 Why This Matters
- **Run AI locally** → no cloud costs, no data leaks.  
- **Learn agent basics** → see how tools, tasks, and models connect.  
- **Portable setup** → same steps work across macOS, Linux, or Windows.  
- **Build confidence** → this is the *“Hello World”* of AI agents.  

---

## ⚙️ Step 0 – Prerequisites: Install Ollama & Model

```bash
# mac
brew install ollama

# linux
curl -fsSL https://ollama.com/install.sh | sh

# pull a small model once
ollama pull mistral
````

**Importance**

* Ollama is the **engine** that runs local models like *Mistral* or *Llama 3*.
* Pulling a model downloads it once → cached on your system.
* This ensures the agent has an “AI brain” to talk to.

---

## 📂 Step 1 – Create a Project Folder

```bash
mkdir agent-poc && cd agent-poc
```

**Importance**

* Keeps files together → easier to manage, share, or push to GitHub.
* Like making a clean workspace before starting a project.

---

## 🐍 Step 2 – Python Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
```

**Importance**

* A **virtual environment** isolates your project dependencies.
* Prevents version conflicts with other Python projects.
* Think of it as a sandbox for your experiment.

---

## 📦 Step 3 – Install Required Libraries

```bash
pip install crewai crewai-tools langchain-ollama
```

**Importance**

* **crewai** → orchestrates agents and tasks.
* **crewai-tools** → gives agents extra abilities (e.g., read files).
* **langchain-ollama** → lets Python talk to Ollama (local LLM server).
* Without these, the agent can’t run.

---

## 📝 Step 4 – Create Sample Content

```bash
cat > sample.md << 'MD'
# Local LLMs – Quick Intro
Local models help keep data private, reduce latency, and avoid per-token cloud costs.
Typical stack: Ollama for models, Markdown for docs, simple CI to publish.
Use cases: summarizing docs, generating checklists, drafting README sections.
MD
```

**Importance**

* Agents need input → here it’s a Markdown file.
* Keeps the POC concrete: read file → process → output summary.

---

## 🤖 Step 5 – Write Minimal Agent Code

```python
# agent.py (or agent_poc.py)

from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import FileReadTool

# 1) Tell CrewAI to use Ollama via LiteLLM
llm = LLM(
    model="ollama/mistral",                  # <-- provider/model
    base_url="http://localhost:11434",       # <-- Ollama default
    temperature=0.2,
)

file_tool = FileReadTool()

summarizer = Agent(
    role="Documentation Summarizer",
    goal="Summarize a local Markdown file in clear bullets.",
    backstory="You are a concise DevOps-friendly technical writer.",
    tools=[file_tool],
    llm=llm,                                  # <-- use CrewAI LLM here
    verbose=True,
    allow_delegation=False,
)

task = Task(
    description=(
        "Read the file at {file_path} and produce:\n"
        "1) TL;DR (3 bullets)\n"
        "2) Key concepts (up to 5 bullets)\n"
        "3) Action checklist (3 items)\n"
        "Keep it short and Markdown-formatted."
    ),
    expected_output="A concise Markdown section with the three parts.",
    agent=summarizer,
)

crew = Crew(
    agents=[summarizer],
    tasks=[task],
    process=Process.sequential,
    verbose=True,
)

if __name__ == "__main__":
    result = crew.kickoff(inputs={"file_path": "sample.md"})
    print("\n=== AGENT OUTPUT ===\n")
    print(result)
```

**Importance**

* **Agent** = the role/persona (here: summarizer).
* **Tool** = ability (read files).
* **Task** = what to do (summarize into 3 sections).
* **Crew** = runs agents + tasks in sequence.
* This shows the *core loop* of any agent system.

---

## ▶️ Step 6 – Run the Agent

```bash
python agent_poc.py
```

**Importance**

* Executes the pipeline end-to-end.
* You’ll see a Markdown summary like:

```markdown
### TL;DR
- Local models keep data private  
- Reduce costs & latency  
- Great for docs and checklists  

### Key Concepts
- Ollama as local model runner  
- Markdown docs as input  
- CI pipelines to publish  

### Action Checklist
- Install Ollama & pull model  
- Run local summarizer  
- Extend with new tools
```

---

## 🔍 How It All Fits Together

```
sample.md ──(FileReadTool)──► Agent Prompt ──► Mistral (Ollama) ──► Markdown Summary
```

* The **tool** reads the file.
* The **agent** turns it into a request.
* The **model** (Mistral) generates the response.
* The **crew** coordinates it all.

---

## ✅ What You Learned

* How to run a **local LLM** (Mistral via Ollama).
* How to define a **basic agent** with CrewAI.
* How to attach a **tool** so the agent can interact with files.
* How to create a **task** and run it end-to-end.

This POC is the “starter kit” → from here you can:

* Add more tools (e.g., directory reader, web scraper).
* Swap models (e.g., `llama3:8b`).
* Automate workflows in CI/CD pipelines.

---

## 🚀 Next Steps

* **Dockerize** this setup for portability.
* **Add GitHub Actions** to auto-run on pull requests.
* **Integrate monitoring** (logs/metrics) for a DevOps-ready agent.

---


