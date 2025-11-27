import asyncio
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_core.messages import ToolMessage
from dotenv import load_dotenv
load_dotenv()


# servers
SERVERS = { 
    "math": {
        "transport": "stdio",
        "command": "/Library/Frameworks/Python.framework/Versions/3.11/bin/uv",
        "args": [
            "run",
            "fastmcp",
            "run",
            "D:\hobby projects\python\MCP servers\expense tracker server\my_local_server.py"
       ]
    },
    "expense": {
        "transport": "streamable_http",  # if this fails, try "sse"
        "url": "https://splendid-gold-dingo.fastmcp.app/mcp"
    },
    "manim-server": {
        "transport": "stdio",
        "command": "/Library/Frameworks/Python.framework/Versions/3.11/bin/python3",
        "args": [
        "/Users/nitish/desktop/manim-mcp-server/src/manim_server.py"
      ],
        "env": {
        "MANIM_EXECUTABLE": "/Library/Frameworks/Python.framework/Versions/3.11/bin/manim"
      }
    }
}



async def main():
    print("Hello World!")


if __name__ == "__main__":
    asyncio.run(main())
