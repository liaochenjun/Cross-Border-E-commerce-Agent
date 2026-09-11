#!/usr/bin/env python3
"""crawl4ai-mcp: MCP server wrapping crawl4ai for URL-to-markdown extraction."""

import asyncio, sys

from mcp.server import MCPServer

server = MCPServer("crawl4ai-mcp", version="0.1.0")

@server.tool()
async def crawl_url(url: str) -> str:
    """Crawl a URL and return clean markdown. Use to extract structured text from web pages."""
    from crawl4ai import AsyncWebCrawler
    try:
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(url=url)
        return result.markdown[:8000] if result.markdown else f"[No markdown from {url}]"
    except Exception as e:
        return f"Crawl error: {str(e)}"

if __name__ == "__main__":
    server.run()