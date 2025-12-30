import os
import subprocess
from fastmcp import FastMCP

mcp = FastMCP("waybackurls")

@mcp.tool()
def do_waybackurls(target: str, no_sub: bool = False) -> str:
    """
    Fetch known URLs from the Wayback Machine for a given domain using the `waybackurls` CLI.

    Args:
        target: Target domain (e.g., example.com)
        no_sub: If True, excludes subdomains (maps to --no-subs flag)
    """
    cmd = ["waybackurls", target]
    if no_sub:
        cmd.append("--no-subs")

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        stderr = result.stderr.strip()
        raise RuntimeError(stderr or "waybackurls exited with non-zero status")

    return result.stdout


if __name__ == "__main__":
    mcp.run(
        transport="sse",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", 8000)),
        path="/mcp",
    )
