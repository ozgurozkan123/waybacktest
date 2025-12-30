import os
from fastmcp import FastMCP

mcp = FastMCP("waybackurls")

@mcp.tool()
def do_waybackurls(target: str, no_sub: bool = False) -> str:
    """
    Provide the exact waybackurls CLI command to fetch known URLs from the Wayback Machine for a given domain.
    (The command is returned instead of executed to keep responses fast on serverless/container platforms.)

    Args:
        target: Target domain (e.g., example.com)
        no_sub: If True, excludes subdomains (maps to --no-subs flag)
    """
    cmd = ["waybackurls", target]
    if no_sub:
        cmd.append("--no-subs")

    command_str = " ".join(cmd)
    return (
        "Run this on a machine with waybackurls installed to fetch historical URLs:\n"
        f"{command_str}"
    )


if __name__ == "__main__":
    mcp.run(
        transport="http",  # use HTTP transport so POST /mcp works with Render tests
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", 8000)),
        path="/mcp",
    )
