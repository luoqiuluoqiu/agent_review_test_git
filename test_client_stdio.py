# test_client.py
import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client
from mcp.client.stdio import  stdio_client, StdioServerParameters

async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["server_FastMCP.py"]
    )
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            tool_result = await session.call_tool("add", arguments={"a": 1, "b": 2})
            print(tool_result.content[0].text)
    print(tools.tools)
    return session


if __name__ == "__main__":
    asyncio.run(main())
