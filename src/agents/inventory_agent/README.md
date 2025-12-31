# Inventory Agent 

This agent is written using the Google Agent Development Kit and the
Python A2A SDK.

## Running the Agent:

1. Create an environment file with your API key:

```shell
echo "GOOGLE_API_KEY=your_api_key_here" > .env
```


2. Run the agent:

```shell
uv run main.py
```


### How it works:

In the `main.py` file we define the `AgentCard`. `AgentCard` is a machine-readable 
JSON metadata document that serves as an agent's digital 
business card or manifest. 


It is a core component of the ADK that enables interoperability and 
dynamic discovery within a multi-agent system. 

The `AgentCard` is crucial for allowing different agents, potentially
built using different frameworks (like LangChain, CrewAI or 
ADK itself) and running on different platforms, to discover 
and interact with each other. in a standardized way.

Key aspects of the `AgentCard` in a python A2A implementation include:

* Standardized Location: The A2A protocol specifies that the 
`AgentCard` should be accessile via a well-known HTTP
  endpoint
  
* Programmatic Access: The python A2A SDK provides classes 
  (like AgentCard and AgentSkill) that allow developers to
  define and serve this information. 


##### Usage in Agentic AI Systems

For an agentic AI system, the `AgentCard` is fundamental for
bulding flexible, scalable and secure multi-agent workflows:

1. Agent Discovery: An A2A client Agent (or an orchestrator) can query the 
`AgentCard` s ov various remote agents to identify which one possesses the 
   specific skills needed for a task, without needing prior knowledge
   of their internal  workings
   
2. This dynamic discovery allows complex tasks to be broken down into 
into sub-tasks and delegated to the most apropriate, specialized 
   agent at run-time, rather than relying on brittle, hardcoded integrations
   


Our `main` function we also define the `DefaultRequestHandler` is a build-in server component provided by the A2A
Pythos SDK within Google's ADK. It acts as the intermediary between incoming A2A HTTP requests from a clinet and the 
internal core logic of the remote agent (the "Agent Executor")

Key Functions:

* Protocol Abstraction: Handles low-level mechanics of the A2A protocol, abstracting away the specifics of HTTP, JSON-RPC 2.0 message format and 
  data serialization
* Request Routing: It receives incoming A2A calls (like execute or cancel a task) and routes them to the appropriate
method within the developer-defined AgentExecutor
  
* Task Management: It uses a TaskStore (y default, an InMemoryTaskStore) to manage the state and lifecycle of ongoing tasks. This is 
crucial for handling long-running, async tasks, streaming updates.

