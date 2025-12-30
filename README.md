# waybacktest

FastMCP server for the `waybackurls` CLI. Built from the original MCP module in `cyproxio/mcp-for-security/waybackurls-mcp`.

## Tools
- `do_waybackurls` — Fetch historical URLs from the Wayback Machine for a domain. Optional `no_sub` flag maps to `--no-subs`.

## Run locally
```bash
docker build -t waybacktest .
docker run -p 8000:8000 waybacktest
```
MCP endpoint: `http://localhost:8000/mcp` (SSE transport)
