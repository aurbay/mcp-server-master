# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


@mcp.tool()
def hello_world() -> str:
    return "hello world"

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


@mcp.tool()
def car_price(model: str, year: int) -> str:
    """Get the price of a car model for a given year"""
    # In a real application, this would query a database or an API
    prices = {
        "Toyota Camry": {2020: "$24,000", 2021: "$25,000"},
        "Honda Accord": {2020: "$23,000", 2021: "$24,500"},
    }
    return prices.get(model, {}).get(year, "Price not available")

if __name__ == "__main__":    
    # Start the MCP server
    mcp.run(transport="stdio")