from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from shipping_tools import get_shipping_info
from agent_utils import retry_config





# Create the Inventory Agent
# This agent specializes in checking stock levels and restocking schedules
product_shipping_agent = LlmAgent(
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    name="inventory_agent",
    description="External vendor's shipping agent that provides information on the existing inventory and restocking schedules.",
    instruction="""
    You are a shipping information agent from an external vendor.
    When asked about products, use the get_shipping_info tool to fetch data from the inventory.
    Provide clear, accurate product information including delivery days and cost, express shipping and expresss shipping cost.
    If asked about multiple products, look up each one.
    Be professional and helpful.
    """,
    tools=[get_shipping_info],  # Register the product lookup tool
)