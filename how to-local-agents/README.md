
# 🚀 POC: Create Your First Local AI Agent with CrewAI + Ollama

This repo shows you how to create and run a **local AI agent** using:
- [CrewAI](https://github.com/joaomdmoura/crewai) – orchestration for multi-agent workflows  
- [Ollama](https://ollama.com/) – run large language models locally  
- Python virtual environments – clean and isolated setup  

It’s written for **beginners** (including non-developers), but also useful for DevOps and advanced users.  

---

## 🌟 Why This Project Matters
- **Run AI locally** → No cloud costs, no API keys, full privacy.  
- **Understand agents** → Learn how tools, tasks, and agents connect.  
- **Reproducible** → Everything isolated in a Python virtual environment.  
- **Extendable** → Add more agents, tools, or plug into CI/CD later.  

---

## ⚙️ Step 0 – Install Ollama & Pull a Model

```bash
# mac
brew install ollama

# linux
curl -fsSL https://ollama.com/install.sh | sh

# windows (PowerShell)
winget install Ollama.Ollama

# pull a small model once (cached locally)
ollama pull mistral
````

✅ **Why:** Ollama is the local LLM engine. Pulling `mistral` ensures you have a small, fast model ready to use.
ℹ️ You don’t need to pull every time. Once cached, it’s reusable.

---

## 📂 Step 1 – Create a Project Folder

```bash
mkdir agent-poc && cd agent-poc
```

✅ **Why:** Keeps all project files organized and portable (good for GitHub/Docker).

---

## 🐍 Step 2 – Setup Python Environment

```bash
python3 -m venv .venv
source .venv/bin/activate     # mac/linux
# .venv\Scripts\activate      # windows (PowerShell)

pip install --upgrade pip
```

✅ **Why:** A virtual environment prevents package conflicts with other projects.

---

## 📦 Step 3 – Install Dependencies

```bash
pip install crewai crewai-tools langchain-ollama
```

✅ **Why:**

* `crewai` → defines agents, tasks, and workflows.
* `crewai-tools` → common tools like FileReadTool, WebSearchTool, etc.
* `langchain-ollama` → bridge between Python and Ollama server.

---

## 📝 Step 4 – Add a Sample Markdown File

```bash
cat > sample.md << 'MD'
# Local LLMs – Quick Intro
Local models help keep data private, reduce latency, and avoid per-token cloud costs.
Typical stack: Ollama for models, Markdown for docs, simple CI to publish.
Use cases: summarizing docs, generating checklists, drafting README sections.
MD
```

✅ **Why:** Agents need input. This gives them a real file to work with.

---

## 🤖 Step 5 – Create the Agent Script

Create a file `agent_poc.py` with the following code:

```python
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import FileReadTool

# Connect to local Ollama model
llm = LLM(model="ollama/mistral", base_url="http://localhost:11434", temperature=0.2)

# Tool for reading local files
file_tool = FileReadTool()

# Define the agent
summarizer = Agent(
    role="Documentation Summarizer",
    goal="Summarize a local Markdown file in clear bullets.",
    backstory="You are a concise DevOps-friendly technical writer.",
    tools=[file_tool],
    llm=llm,
    verbose=True,
)

# Define the task
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

# Define the crew
crew = Crew(
    name="DocOps Crew",
    description="Summarizes and analyzes local Markdown files",
    agents=[summarizer],
    tasks=[task],
    process=Process.sequential,
    verbose=True,
    memory=True,
    output_log_file="crew_output.log"
)

if __name__ == "__main__":
    result = crew.kickoff(inputs={"file_path": "sample.md"})
    print("\n=== AGENT OUTPUT ===\n")
    print(result)
```

✅ **Why:** This is the “glue” that ties agents, tools, and tasks together.

---

## ▶️ Step 6 – Run It

```bash
python agent_poc.py
```

You’ll see:

* Execution logs (because `verbose=True`)
* A neat Markdown summary printed to your terminal

Example output:

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

## 🔧 Crew Parameters Explained

Here are the most useful parameters for `Crew(...)`:

| Parameter         | Type | Default      | Purpose                                                                  | Example                                   |
| ----------------- | ---- | ------------ | ------------------------------------------------------------------------ | ----------------------------------------- |
| `agents`          | list | *required*   | Which agents to include in the crew                                      | `[summarizer, risk_analyst]`              |
| `tasks`           | list | *required*   | Which tasks to execute                                                   | `[task1, task2]`                          |
| `process`         | enum | `sequential` | Execution style: `sequential` or `concurrent`                            | `process=Process.concurrent`              |
| `verbose`         | bool | `False`      | Show detailed logs during execution                                      | `verbose=True`                            |
| `memory`          | bool | `False`      | Share context between tasks (later tasks see earlier outputs)            | `memory=True`                             |
| `max_rpm`         | int  | None         | Limit requests per minute (useful for rate-limited APIs, not local LLMs) | `max_rpm=60`                              |
| `output_log_file` | str  | None         | Save outputs to a file                                                   | `"crew_output.log"`                       |
| `name`            | str  | None         | Human-friendly crew name                                                 | `"DocOps Crew"`                           |
| `description`     | str  | None         | Explain what the crew does                                               | `"Summarizes and analyzes documentation"` |

---

## ✅ What You’ve Learned

* How to **install Ollama** and pull a model
* How to **set up Python + CrewAI**
* How to **define an agent, tool, and task**
* How to **run a crew and review its output**
* The meaning of key **Crew parameters**

---

## 🚀 Next Steps

* Add more tasks (e.g., generate FAQ, risk analysis, compliance checks).
* Add more agents (e.g., “Risk Analyst”, “Communicator”).
* Containerize with **Docker** for portability.
* Integrate into **GitHub Actions** to auto-run on pull requests.

---

## 🧩 Troubleshooting

* **Error: connection refused on port 11434** → Ollama isn’t running → run `ollama run mistral "hi"` once to auto-start it.
* **ModuleNotFoundError** → Ensure your venv is active (`source .venv/bin/activate`).
* **Empty output** → Ensure `sample.md` exists in the same folder.

---

Happy hacking! 
This is your **first working CrewAI agent running locally**. From here, you can extend it into a full multi-agent workflow.

```
