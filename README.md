# Cross-Border E-commerce AI Agent | 跨境电商 AI Agent 系统

> 不是做一个"会聊天的跨境电商 AI"，而是做一个能持续运行跨境电商业务流程的 Agent Operating System。

## 核心目标

用户提出一个商业目标：

> "帮我找到一个适合日本市场的产品并完成从选品到销售的流程。"

Agent 自动完成：

```text
目标理解 → 任务拆解 → 工具选择 → MCP 调用
→ 市场研究 → 供应商搜索 → 成本计算 → 产品管理
→ 上架 → 订单 → 物流 → 客服 → 数据分析
```

## 当前阶段：V0.1 — Information Agent

当前重点：Search / Playwright / Crawl4AI（网页转 Markdown 的 MCP 封装见 `.claude/mcp-servers/crawl4ai-mcp/`，安装与依赖说明见该目录 `README.md`）。

> 上表链路中的其余环节（供应商、成本、上架、订单、物流、客服、分析等）均为设计目标，**尚未实现**。

## 技术路线

- LLM：Qwen3.8-Flash
- 工具接入层：MCP
- 信息采集：Search / Playwright / Crawl4AI
- 供应商：1688 Adapter / MCP（计划）
- 成本利润：Cost / Profit Engine（计划，确定性计算引擎，不交给 LLM 算账）
- 商业基础：Medusa 作为 Commerce Core 候选（计划）
- 销售渠道、物流、客服、营销：后续逐步增加

## 目录结构

```text
.claude/
├── skills/                          供 Claude Code 加载的项目知识
│   ├── architecture.md                  系统架构设计（主文档）
│   ├── cross-border-capability-map/     36 个业务模块开源能力地图
│   ├── ecomm-kb/                        原跨境电商知识库的蒸馏知识
│   └── reuse-oss/                       「优先复用开源」工作流 + 评估清单
└── mcp-servers/
    └── crawl4ai-mcp/                网页转 Markdown 的 MCP server

0基础小白跨界电商知识库.md            原知识库全文（存档）
README.md
LICENSE
```

## 架构与设计资产

- `.claude/skills/architecture.md` — 系统架构设计（主 Agent + 业务 Agent + MCP/Adapter + Commerce Core + 事件驱动 + 人工审批边界）
- `.claude/skills/cross-border-capability-map/` — 36 个业务模块开源能力地图（2026-09 GitHub API 实测，A/B/C/D 分级）
- `.claude/skills/reuse-oss/` — 「优先复用开源」工作流与候选项目评估清单
- `.claude/skills/ecomm-kb/` — 原「跨境电商知识库」的蒸馏知识（业务背景参照，非本仓库产物）

架构最高原则：**Agent 是大脑，MCP 是接口，Adapter 是翻译层，Business Core 是业务执行系统，Database 是事实来源，Event 是触发机制，Human Approval 是风险边界。**

## 项目渊源

本仓库独立新建（另起炉灶），不继承原「跨境电商知识库」的 Git 历史；网络环境文档（路由器代理 / Clash 配置）不在本仓库范围内。

## 免责声明

内容仅供学习与参考，不构成法律、税务或投资建议；涉及的网络与自动化技术仅用于跨境电商运营的合法合规需求。

## 许可与来源

本仓库内容整体采用 **CC BY-NC-SA 4.0**（署名 — 非商业性使用 — 相同方式共享），全文见 [`LICENSE`](LICENSE)：转载须署名，禁止打包售卖或用于付费培训，衍生作品须以相同协议发布。

例外：`.claude/skills/reuse-oss/references/` 评估清单拷贝自 [mcpserver-finder](https://github.com/ModelContextProtocol-Security/mcpserver-finder)，保持其 **Apache-2.0** 许可（见该目录 `SOURCE.md`）。
