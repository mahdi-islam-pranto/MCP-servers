from fastmcp import FastMCP

# create a FastMCP instance
mcp = FastMCP("My First Server")

# define a tool
@mcp.tool
def greet(name: str) -> str:
    return f"Hello, lala, {name}!"

if __name__ == "__main__":
    mcp.run()

