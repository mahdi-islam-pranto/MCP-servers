from fastmcp import FastMCP

mcp = FastMCP("Mahdi's test server")

# number adding tool
@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# generate random number tool
import random
@mcp.tool
def random_number(a: int, b: int) -> int:
    """Generate a random number"""
    return random.randint(a, b)
    
# run the server remotely
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
