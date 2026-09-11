---
name: reuse-oss
description: 本仓库开发新功能时的强制工作流:优先复用 GitHub 成熟开源项目,而不是重复造轮子。当用户提出新功能需求、或准备编写较大功能模块时,先走"搜索 → 评估 → 汇报确认 → 集成 → 验证"流程。涉及 MCP Server / SDK / Plugin / Library 选型时同样适用。
---

# 优先复用开源 (Reuse OSS First) 工作流

> 用户定下的开发原则:优先集成 GitHub 成熟开源项目,而非自研。目标是成为"搜索 GitHub → 发现成熟项目 → 分析 → 选择方案 → 自动集成 → 测试验证"的开发代理,而不是写尽可能多的代码。

## 核心规则

1. 新功能先判断 GitHub 是否已有成熟的开源项目 / SDK / MCP Server / Plugin / 工具可以实现。
2. **不要一开始就编写完整实现。**
3. 第一个候选不合适 → 继续搜索其他项目,**不要立即转自研**。
4. 只有确认 GitHub 没有合适的现成项目、或现有项目无法满足需求时,才自行开发。
5. 集成时保持当前项目架构,不因引入一个工具而大规模重构。
6. 准备自己编写较大功能模块前,先问:"GitHub 上有没有已经实现这个功能的成熟项目?"

## 流程

```
我的需求
  ↓ 分析需要什么能力
  ↓ 搜索 GitHub
  ↓ 搜索现有 MCP / SDK / Plugin / Library
  ↓ 找到多个候选项目
  ↓ 检查 Star、最近更新时间、Issue、PR、License、技术栈、文档
  ↓ 判断是否可直接集成
  ↓ 选择最合适的项目
  ↓ Clone / 安装 / 配置
  ↓ 集成到当前项目
  ↓ 运行测试
  ↓ 确认功能正常
```

## 搜索工具(按优先级)

1. **GitHub 官方 MCP Server**:`github/github-mcp-server` — 搜索 Repository / Code、读 README 与文件、看 Issues / PR、分析项目结构。
   - 已在 Claude Code 配置为 MCP server `github`(user 全局,Remote 模式 + PAT)。
   - 未配置时回退方案:`gh` CLI(`gh search repos` / `gh api`)、WebSearch(`site:github.com` 关键词)、WebFetch GitHub 页面或 API(`api.github.com/search/repositories`)。
2. **项目发现**:`Vvkmnn/claude-oracle-mcp` — 一次搜索 17 个注册表(15000+ skills/plugins/MCP),零配置无需 API key。
   - 已在 Claude Code 配置为 MCP server `claude-oracle-mcp`(user 全局,stdio via npx)。
3. **MCP Server 评估**:`ModelContextProtocol-Security/mcpserver-finder` 的检查清单已并入本 skill(`references/` 目录,Apache-2.0),用于评估候选项目质量。评估时对照以下清单:
   - `references/github-repository-health.md` — 仓库健康(活跃度、维护状态)
   - `references/code-quality-assessment.md` — 代码质量
   - `references/test-quality-assessment.md` — 测试质量
   - `references/dependency-management-assessment.md` — 依赖管理
   - `references/CHECK-TEMPLATE.md` — 检查模板

## 项目选择标准(综合判断,Star 高不等于合适)

- 项目成熟度、Star 数量、最近更新时间、Commit 活跃程度
- Issue / PR 情况(响应与维护状态)
- **License 是否允许当前项目使用**
- 完整 README、实际使用案例
- 与当前项目技术栈兼容、易安装维护
- **可直接集成**,而非需要大量修改源码
- 深入评估时对照 `references/` 下的检查清单逐项打分

## 强制汇报门槛(每次采用第三方项目前)

必须先向用户汇报以下内容,**确认方案合理后,再进行实际集成**:

1. 找到了哪些候选项目
2. 各项目 GitHub 地址
3. 每个项目的用途
4. 为什么选择其中一个
5. 如何集成(Clone / npm / pip / Maven / Docker / MCP / SDK / Git Submodule)
6. 是否存在 License 或兼容性问题

## License 注意事项

- 本仓库内容采用 **CC BY-NC-SA 4.0**(署名、非商业、相同方式共享)。
- 引入第三方代码/工具时核对其 License 与本仓库用途是否冲突,重点留意:GPL 传染性、非商业限制、再分发要求。
- 仅"作为工具使用"与"将代码并入仓库"的许可要求不同,选择时区分对待。

## 已知问题与排障(2026-09-12 实测)

- `claude mcp list` 健康检查可能显示 github server "Connected · tools fetch failed — MCP error -32001":这是代理网络下 tools/list(约 130KB 响应)首拉较慢所致;**实际工具调用正常**(search_repositories 实测 1.3s 返回 200),可忽略该健康检查报错。
- 若实际调用也超时,再排查:settings.json 提高 `MCP_TIMEOUT`、检查路由器节点对 `api.githubcopilot.com` 的路由质量,或改用本地二进制 stdio 模式。
- 新增 MCP server 后,工具要在**新会话**(或重连)中才会出现在可用工具列表里。
- claude-oracle-mcp 用 npx 首次下载会超 30s 连接超时,已 `npm install -g claude-oracle-mcp` 预热解决;新机器部署时先全局安装再 `claude mcp add`。
