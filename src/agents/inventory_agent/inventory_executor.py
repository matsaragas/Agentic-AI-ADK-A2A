from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.server.tasks import TaskUpdater
from a2a.types import Part, TaskState, TextPart
from google.adk.runners import Runner
from google.adk.artifacts import InMemoryArtifactService
from google.adk.sessions import InMemorySessionService
from google.adk.memory.in_memory_memory_service import InMemoryMemoryService
from a2a.utils import new_agent_text_message, new_task
from google.genai import types


class InventoryAgentExecutor(AgentExecutor):

    def __init__(self,
                 agent,
                 status_message="processing request...",
                 artifact_name="response"):
        super().__init__()
        self.agent = agent
        self.status_message = status_message
        self.artifact_name = artifact_name

        self.runner = Runner(
            app_name=agent.name,
            agent=agent,
            artifact_service=InMemoryArtifactService(),
            session_service=InMemorySessionService(),
            memory_service=InMemoryMemoryService(),
        )