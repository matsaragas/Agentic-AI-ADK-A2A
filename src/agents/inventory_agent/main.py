
import logging
import click
import uvicorn
from inventory_agent import inventory_product_agent
from a2a.server.apps import A2AStarletteApplication
from a2a.types import (
    AgentCapabilities,
    AgentCard,
    AgentSkill,
)
from a2a.server.tasks import InMemoryTaskStore
from a2a.server.request_handlers import DefaultRequestHandler
from inventory_executor import InventoryAgentExecutor
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MissingAPIKeyError(Exception):
    """Exception from missing API key"""

@click.command()
@click.option("--host", default="localhost")
@click.option("--port", default=10001)
def main(host, port):

    agent_card = AgentCard(
        name="Product Catalog Agent",
        description=inventory_product_agent.description,
        url=f'http://{host}:{port}',
        version="1.0.0",
        defaultInputModes=["text", "text/plain"],
        defaultOutputModes=["text", "text/plain"],
        skills=[
            AgentSkill(
                id="inventory_product_provider",
                name="Inventory Provider",
                description="Provides inventory information of the available products",
                tags=["inventiry", "product"],
                examples=[
                    "Can you tell me about the iPhone 15 Pro? Is it in stock?",
                    "I'm looking for a laptop. Can you compare the Dell XPS 15 and MacBook Pro 14 for me?",
                    "Do you have the Sony WH-1000XM5 headphones? What's the price?"
                ],
            )
        ],

    )

    request_handler = DefaultRequestHandler(
        agent_executor=InventoryAgentExecutor(
            agent=inventory_product_agent,
        ),
        task_store=InMemoryTaskStore(),
    )

    server = A2AStarletteApplication(
        agent_card=agent_card, http_handler=request_handler
    )

    uvicorn.run(server.build(), host=host, port=port)

if __name__ == "__main__":
    main()