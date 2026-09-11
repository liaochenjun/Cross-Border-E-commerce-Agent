# crawl4ai-mcp

把 [crawl4ai](https://github.com/unclecode/crawl4ai) 封装成 MCP server，向 Agent 暴露一个 `crawl_url` 工具：抓取网页并返回清洗后的 Markdown 正文。

属于本项目 V0.1（Information Agent）阶段的信息采集能力，与 Search、Playwright 并列。

## 工具

| 工具 | 签名 | 说明 |
| :--- | :--- | :--- |
| `crawl_url` | `(url: str) -> str` | 抓取 `url`，返回 Markdown 正文，最长 8000 字符。失败时返回 `Crawl error: ...` 字符串，不抛异常。 |

## 安装

```shell
python -m pip install -r .claude/mcp-servers/crawl4ai-mcp/requirements.txt
```

`crawl4ai` 依赖 Playwright 的浏览器内核，首次使用前需要单独装一次：

```shell
crawl4ai-setup
```

## 运行

```shell
python .claude/mcp-servers/crawl4ai-mcp/server.py
```

它以 stdio 方式对外提供服务，通常不由人手动启动，而是由 MCP 客户端读取仓库根目录的 `.mcp.json` 拉起：

```json
{
  "mcpServers": {
    "crawl4ai": {
      "type": "stdio",
      "command": "python",
      "args": [".claude/mcp-servers/crawl4ai-mcp/server.py"],
      "env": { "PYTHONUNBUFFERED": "1" }
    }
  }
}
```

用 `claude mcp list` 检查连通性，用 `/mcp` 查看并批准项目级 server（`.mcp.json` 随仓库下发，首次使用需要手动批准一次）。

### 路径解析注意事项

`args` 里用的是**相对路径**，因此需要在**仓库根目录**启动 Claude Code 才能解析到。两点实测记录：

- **不要改用 `${CLAUDE_PROJECT_DIR}`**。在 Claude Code 2.1.269 上该变量不会展开，`claude mcp list` 会直接报 `Missing environment variables: CLAUDE_PROJECT_DIR`。作为 `.mcp.json` 的写法不可用。
- 如果从子目录启动、导致相对路径解析失败，把 `args` 换成该脚本的绝对路径即可（代价是换机器要改）。

## 依赖版本约束

`server.py` 用的是 `mcp.server.MCPServer`。这个类在 MCP Python SDK **v2** 中由 v1 的 `FastMCP` 改名而来，因此 **必须 `mcp >= 2`**；装成 mcp 1.x 会在 import 阶段直接报错。`requirements.txt` 里已按此约束固定下限。

## 已知限制

- 返回正文截断在 8000 字符，长文需要自行分页或加摘要。
- 未做 robots.txt / 频控处理，接入批量抓取前需要补。
- 无缓存，同一 URL 重复调用会重复抓取。
