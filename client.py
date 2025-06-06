# Create server parameters for stdio connection
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


import asyncio
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent

from dotenv import load_dotenv
load_dotenv()

async def main():
    server_params = StdioServerParameters(
        command="python",
        # Make sure to update to the full absolute path to your math_server.py file
        args=["teams/xyz/server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)

            # Create and run the agent
            #agent = create_react_agent("openai:gpt-4.1", tools)
            agent = create_react_agent("google_genai:gemini-2.0-flash", tools)
            agent_response = await agent.ainvoke({"messages": "what's the price of a Toyota Camry in 2020?"})
            responses = agent_response.get("messages", [])            
            print(responses[-1].content)
            
if __name__ == "__main__":
    asyncio.run(main())