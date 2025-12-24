from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.server.tasks import TaskUpdater
from agent.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.memory.in_memory_memory_service import InMemoryMemoryService
from a2a.utils import new_agent_text_message, new_task



class ProductAgentExecutor(AgentExecutor):

    def __init__(self,
                 agent,
                 status_message="processing request..."):
        super().__init__()
        self.agent = agent
        self.status_message = status_message

        self.runner = Runner(
            app_name=agent.name,
            session_service=InMemorySessionService(),
            memory_service=InMemoryMemoryService(),
        )


    async def execute(self,
                      context: RequestContext,
                      event_queue: EventQueue) -> None:

        query = context.get_user_input()
        task = context.current_task or new_task(context.message)
        await event_queue.enqueue_event(task)

        updater = TaskUpdater(event_queue, task.id, task.context_id)

        if context.call_context:
            user_id = context.call_context.user.user_name
        else:
            user_id = "a2a_user"




