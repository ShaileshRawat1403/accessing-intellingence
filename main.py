import os
from dotenv import load_dotenv
from agent_config import get_agent_executor
import agentops

# Load .env variables
load_dotenv()

# Initialize AgentOps and store the trace context
trace_context = agentops.init(api_key=os.getenv("AGENT_OPS_KEY"))

# Get your Runnable chain
chain = get_agent_executor()

# User query
query = "I like the following artists: Drake, Future. Can I get 5 song recommendations?"

# Run agent safely
try:
    print("\n🎧 Running modern LLM agent...\n")
    response = chain.invoke(query)
    print("\n🎵 Final Song Recommendations:\n")
    print(getattr(response, "content", response))
finally:
    if trace_context:
        agentops.end_trace(trace_context, "Completed")
