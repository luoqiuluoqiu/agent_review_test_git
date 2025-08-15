# test_client.py
import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

async def main():
    async with sse_client("http://localhost:8000/sse") as streams:
        async with ClientSession(streams[0], streams[1]) as session:
            await session.initialize()
            tools = await session.list_tools()
            tool_result = await session.call_tool("add", arguments={"a": 1, "b": 2})
            print(tool_result.content[0].text)
    print(tools.tools)
    return session
if __name__ == "__main__":
    asyncio.run(main())