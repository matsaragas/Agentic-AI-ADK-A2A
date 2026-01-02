
import logging
import click
import uvicorn
from shipping_agent import product_shipping_agent
from a2a.server.apps import A2AStarletteApplication
from a2a.types import (
    AgentCapabilities,
    AgentCard,
    AgentSkill,
)
from a2a.server.tasks import InMemoryTaskStore
from a2a.server.request_handlers import DefaultRequestHandler
from shipping_executor import ShippingAgentExecutor
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MissingAPIKeyError(Exception):
    """Exception from missing API key"""

@click.command()
@click.option("--host", default="localhost")
@click.option("--port", default=10003)
def main(host, port):

    agent_card = AgentCard(
        name="Product Shipping Agent",
        description=product_shipping_agent.description,
        url=f'http://{host}:{port}',
        version="1.0.0",
        defaultInputModes=["text", "text/plain"],
        defaultOutputModes=["text", "text/plain"],
        capabilities=AgentCapabilities(streaming=True),
        skills=[
            AgentSkill(
                id="shipping_product_provider",
                name="Shipping Information Provider",
                description="Provides shipping information of the available products",
                tags=["shipping", "product"],
                examples=[
                    "Can you tell me the usual delivery days and shipping cost for iPhone 15 Pro?",
                    "Can you compare the express delivery days between Dell XPS 15 and MacBook Pro 14 for me?",
                    "What is the express delivery info for ipad air?"
                ],
            )
        ],

    )

    request_handler = DefaultRequestHandler(
        agent_executor=ShippingAgentExecutor(
            agent=product_shipping_agent,
        ),
        task_store=InMemoryTaskStore(),
    )

    server = A2AStarletteApplication(
        agent_card=agent_card, http_handler=request_handler
    )

    uvicorn.run(server.build(), host=host, port=port)

if __name__ == "__main__":
    main()