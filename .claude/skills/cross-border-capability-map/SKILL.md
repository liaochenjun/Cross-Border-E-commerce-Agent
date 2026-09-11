---
name: cross-border-capability-map
description: 跨境电商开源能力地图(2026-09 实测版)。按 36 个业务模块整理 GitHub 开源候选项目,含 stars/license/技术栈/维护状态/集成难度/ABCD 分级,所有数据来自 GitHub API 实测。覆盖 ERP/OMS/库存/采购/利润/客服/CRM/邮件/营销/SEO/广告/分析/渠道连接器等。当需要为某个业务模块选型开源项目、评估 License 风险、或参考代理化(MCP)路径时使用。
---

# 跨境电商开源能力地图

> ✅ 2026-09-11~12 调研全部完成,5/5 组数据齐全。
> 所有数据来自 GitHub REST API 实测(带 PAT 鉴权)。`NOASSERTION`=API 无法识别 SPDX,已逐个拉 LICENSE 原文核实。
>
> 分类:A=可直接集成 B=参考/抽取模块 C=以后集成 D=不建议

---

## 检索策略与项目筛选规则

> 硬性规则,目的是避免后台 Agent 为凑数量消耗大量 Token。**宁可少找,不要滥搜。**

### 一、Star 数量门槛(按业务领域分级)

| 业务领域 | 最低 Stars | 例外 |
|---|---|---|
| **Agent / MCP / Browser / Search / Agent Infrastructure** | ≥ 5,000 | 官方项目、官方 SDK、官方 MCP Server 可突破 |
| **电商核心平台**(Headless Commerce / ERP / OMS / PIM / Marketplace 平台) | ≥ 3,000 | 同上 |
| **Marketplace SDK / API / 数据采集 / 选品工具** | ≥ 1,000 | 同上 |
| **翻译 / 物流 / 支付 / 邮件** 等垂直工具 | ≥ 500 | 同上 |
| **< 500 Stars** | 仅允许检索 | 官方项目、官方 SDK、官方 MCP、或某个非常垂直且无成熟替代方案的关键能力 |
| **< 100 Stars** | **默认直接跳过** | 除非是官方项目或官方 SDK |

### 二、维护状态门槛

即使 Stars 达标,以下情况**降低优先级或直接跳过**:

- 最后提交距今 > 12 个月(无活跃维护信号)
- `archived: true`(GitHub 已归档)→ **直接跳过**
- README 明确标注 deprecated / unmaintained / migrated → **直接跳过**
- Issues 长期堆积无人处理(例:5k+ Stars 但对 0 Star 项目有 > 1000 open issues 且无近期 close 活动) → 降级
- 代码仓库已迁移到新地址 → 只记录新地址,跳过旧仓库

### 三、检索深度(两阶段)

**第一阶段:快速筛选**(每个候选仅检查以下字段,不打开额外文件):
- Stars / Forks
- 最近提交时间(`pushed_at`)
- License(SPDX)
- 是否已归档(`archived`)
- 项目定位(`description`)
- 是否官方(org 归属 / README 首屏)
- 是否有 API / SDK / MCP(从 description 和 topics 判断)
- 技术栈(`language`)

**第二阶段:深度分析**——仅对**通过第一阶段筛选并进入候选名单**的项目进行:
- 读取 README(限首 4000 字符)
- 核验 LICENSE 文件原文(当 API 返回 `NOASSERTION` 时)
- 检查 MCP/server.json 或相关配置
- 检查 OpenAPI/Swagger 文件或 API 文档链接

### 四、候选数量上限

每个业务模块最多保留:
- **3 个主候选**(推荐首选 + 备选)
- **2 个补充参考**(仅记录,不深度分析)

不要为了"36 个模块全部有项目"而无限增加候选。

### 五、核心原则

**宁可少找,也不要大量检索低质量 GitHub 项目。**

最终目标不是 GitHub 项目收藏数量最大化,而是找到**真正适合构建跨境电商 Agent 的成熟能力**。

优先级排序:

```
官方项目/官方 SDK/官方 MCP > 活跃成熟项目 > 高 Star 项目 > 小众垂直项目(仅在无替代时)
```

每发现一个候选,先问:**这个项目真的能帮一个个人/小团队的跨境电商 AI Agent 系统落地吗?** 不能 → 跳过。

---

## 模块速查总表

| # | 业务模块 | 推荐项目 | 分类 | Stars | License | 技术栈 | 一句话理由 |
|---|---|---|---|---|---|---|---|
| 01 | 市场研究 | every-app/open-seo | B | 18.4k | MIT | TypeScript | 自带 MCP+Agent Skills,但数据需自备 DataForSEO API key(付费);开源提供 UI 与 Agent 层 |
| 02 | 关键词研究 | joshcarty/google-searchconsole | B | 254 | MIT | Python | Google Search Console 官方数据(免费合规);google-ads-python 的 KeywordPlanIdeaService 是唯一官方搜索量来源(需广告账户) |
| 03 | 选品 | —(商业 SaaS 垄断) | — | — | — | — | Keepa/Helium10/JungleScout/Sorftime 均为商业 SaaS,开源替代极少;如实报告,不硬凑 |
| 04 | 竞品分析 | —(商业 SaaS 垄断) | — | — | — | — | 同上;OpenSEO 走 DataForSEO 可部分替代外链/排名,不自带数据 |
| 05 | 供应商搜索 | —(1688 合规走 ISV) | — | — | — | — | 1688 开放平台需企业 ISV 签约;GitHub 无官方 SDK;MTOP 逆向库法律高危,标 D |
| 06 | 供应商管理 | inventree/InvenTree + 自研 | A | 7.6k | MIT | Python/Django | 库存底座可扩展供应商字段,已有官方 MCP |
| 07 | 商品/SKU 管理 | **medusajs/medusa** | **A** | 36.3k | **MIT** | TypeScript/Node | 模块化 commerce 平台,官方 MCP+Agent Skills,API-first |
| 07 | 商品/SKU(备选) | saleor/saleor | A | 23.3k | BSD-3 | Python/Django | GraphQL+官方 MCP,多仓库多币种 |
| 08 | 商品内容生成 | ollama/ollama(本地 LLM) | A | 180.7k | MIT | Go | 本地 LLM 服务,OpenAI 兼容 API,支撑 AIGC 内容生成 |
| 09 | 多语言翻译 | **LibreTranslate/LibreTranslate** | **A** | 16.3k | AGPL-3.0 | Python | 自托管 REST 翻译 API;AGPL→自用无碍 |
| 09 | 翻译(质量优先) | OwO-Network/DLX(原 DeepLX) | B | 8.7k | MIT | Go | 反代 DeepL 免费高质量;ToS 风险仅限内部使用 |
| 09 | 翻译(离线兜底) | argosopentech/argos-translate | B | 6.5k | MIT | Python | 纯离线神经翻译,质量中等 |
| 10 | 商品发布(Amazon) | saleweaver/python-amazon-sp-api | A | 680 | MIT | Python | SP-API 全服务封装,当日仍推送,issues 仅 2 |
| 10 | 商品发布(Shopify) | 官方 Shopify/shopify_python_api + GeLi2001/shopify-mcp | A | 1.4k+238 | MIT | Python+MCP | 官方 SDK+现成 MCP server |
| 10 | 商品发布(eBay) | YosefHayim/ebay-mcp | A | 153 | MIT | MCP | eBay Sell REST API MCP,OAuth,2026-08 活跃 |
| 10 | 商品发布(东南亚) | easycb/easycb-go | A | 165 | MIT | Go | 一库覆盖 Lazada/TikTok Shop/Shopee/Shein/Ozon |
| 11 | 定价 | —(无独立引擎) | — | — | — | — | 依赖 ERP 成本字段+自研算法;Amazon repricer 开源已死(最高 5★) |
| 12 | 成本核算 | 自研(参考 CrossBorder-ERP-Lite 口径) | — | — | — | — | CrossBorder-ERP-Lite README 列出了完整的跨境成本项(货值/运费/平台费/FBA/关税/VAT/退货),可抄口径 |
| 13 | 利润计算 | 自研薄层 + InvenTree/Odoo 成本数据 | — | — | — | — | 利润计算无成熟开源;最适合 AI Agent 自研(纯计算+费率表+汇率) |
| 14 | 库存管理 | **inventree/InvenTree** | **A** | 7.6k | **MIT** | Python/Django | 官方 MCP 已就绪(inventree/inventree-mcp),API-first,REST+Python SDK;同类唯一 MIT |
| 14 | 库存(备选) | Part-DB/Part-DB-server | C | 1.8k | AGPL-3.0 | PHP | 功能不错但 AGPL;仅自用可考虑 |
| 15 | 采购管理 | **odoo/odoo Community + erpipe-org/mcp-odoo** | **A** | 54.3k | **LGPL-3.0** | Python | 20年成熟采购模块(询价/采购单/收货/供应商价目表/多币种);社区已有 2 个高星 MCP Server(408★,384★) |
| 16 | 订单管理 | **medusajs/medusa** | **A** | 36.3k | MIT | TypeScript/Node | 官方 MCP+Agent Skills,模块化订单引擎,API-first |
| 16 | 订单(备选) | saleor/saleor | A | 23.3k | BSD-3 | Python/Django | GraphQL+官方 MCP,多渠道多仓库 |
| 17 | 支付(Stripe) | **stripe/ai**(原 agent-toolkit) | **A** | 1.8k | MIT | TypeScript | Stripe **官方** MCP Server+Agent 工具包 |
| 17 | 支付(PayPal) | paypal/paypal-mcp-server | D | 12 | Apache-2.0 | Python | 近一年无推送,基本停滞;用官方 REST SDK 自建 |
| 17 | 支付(订阅计费) | killbill/killbill | B | 5.7k | Apache-2.0 | Java | 支付编排/订阅计费平台,重,适合参考架构 |
| 18 | CRM | **twentyhq/twenty** | **A** | 56.6k | AGPL 核心+MIT SDK | TypeScript | "为 AI 设计的 Salesforce 替代",GraphQL;SDK/UI 包 MIT,可闭源集成;已有 102★ MCP |
| 18 | CRM(纯闭源) | krayin/laravel-crm | A | 23.9k | **MIT** | PHP/Laravel | 多租户,全 MIT,适合要求零 copyleft 的场景 |
| 18 | CRM(轻量) | Django-CRM/BottleCRM | A | 2.4k | **MIT** | Django+SvelteKit | REST+Swagger/OpenAPI,MCP 化极方便;个人/小团队最优 |
| 18 | CRM(架构参考) | trycompai/crm | B | 10.2k | **MIT** | TypeScript | "Agentic-first CRM",内置 agent,无 API key 也可跑 |
| 19 | 客服 | **chatwoot/chatwoot** | **A** | 36.7k | MIT 核心(+enterprise/ 商业) | Ruby+Rails+Vue | 全渠道(邮件/聊天/WhatsApp/FB/IG/Telegram),REST API 完善,社区已有 3 个 MCP |
| 19 | 客服(轻量) | abhinavxd/libredesk | A | 2.9k | AGPL-3.0 | Go 单二进制 | 最轻自托管客服;AGPL 仅限自用 |
| 20 | 邮件(营销) | **knadh/listmonk** | **A** | 23.4k | AGPL-3.0 | Go 单二进制 | 邮件 Newsletter,REST API+已有 MCP(38★);AGPL→自用无碍,SaaS 需开源修改 |
| 20 | 邮件(投递) | **postalserver/postal** | **A** | 16.8k | **MIT** | Ruby | 自建 MTA,DKIM/SPF/退信/Webhook;许可完全宽松 |
| 20 | 邮件(旅程) | dittofeed/dittofeed | B | 2.9k | **MIT** | TypeScript | 行为触发多渠道旅程(邮件/SMS/Push),适合弃购召回/物流通知 |
| 21 | 营销自动化 | **mautic/mautic** | **B** | 10.5k | GPL-3.0 | PHP/Symfony | 全功能营销自动化(邮件/落地页/线索打分/campaign);GPL(非 AGPL)→SaaS 相对安全 |
| 21 | 营销(WhatsApp/IG) | matiasbattocchia/open-bsp-api | A | 569 | **Unlicense** | Deno+Postgres | WhatsApp+IG 自托管平台,面向 AI agent,公共领域,完全自由 |
| 22 | SEO(第一方) | **crawlseo/crawlseo** | **A** | 582 | **MIT** | TypeScript | GSC+爬虫+CWV 一体看板,**自带 MCP Server**,最实用的自托管 SEO |
| 22 | SEO(审计) | every-app/open-seo | B | 18.4k | MIT | TypeScript | 自带 MCP+Agent Skills,但需自备 DataForSEO(付费) |
| 22 | SEO(技术审计) | janreges/siteone-crawler | B | 901 | MIT | Rust | 跨平台爬虫,SEO/安全/可访问性/性能 |
| 23 | 广告(Google) | **googleads/google-ads-mcp** | **A** | 933 | **Apache-2.0** | Python | Google **官方** MCP Server,OAuth 直连 Google Ads API |
| 23 | 广告(Meta) | pipeboard-co/meta-ads-mcp | A | 1.3k | 待核实 | Python | 最流行第三方 Meta Ads MCP;另有 facebook-python-business-sdk(1.6k★,官方) |
| 23 | 广告(Amazon) | denisneuf/python-amazon-ad-api | A | 201 | **MIT** | Python | Amazon Advertising API,95% 覆盖率;KuudoAI/amazon_ads_mcp(69★,MIT)配套 |
| 23 | 广告(TikTok) | AdsMCP/tiktok-ads-mcp-server | B | 49 | MIT | Python | TikTok 营销 API MCP |
| 23 | 广告(多平台索引) | itallstartedwithaidea/advertising-hub | C | 39 | MIT | Markdown | 14 个广告平台 API/MCP/Agent 导航库,做调研索引有用 |
| 24 | 物流(渠道 API) | 各平台 SP-API/官方 SDK | B | — | — | — | Amazon SP-API 含物流;Shopify/eBay 官方 SDK;ShipEngine OpenAPI 可自生成 |
| 25 | 清关/税费(VAT) | pH-7/eu-vat-validator(参考) | B | 98 | GPL-3.0 | PHP | VIES 税号校验;已停更,仅作逻辑参考 |
| 25 | 清关/税费 | **VIES 官方 API + 各国海关公开税率表** | — | — | — | — | 无成熟开源;用 VIES SOAP API(免费)自建工具;HS 归类用 LLM+公开 HS6 表 |
| 26 | 订单履约 | Medusa/Saleor 订单引擎 + 自研流程 | B | — | — | — | Headless commerce 内置订单状态机,履约流程需自研 |
| 27 | 物流追踪 | **无生产级开源** | — | — | — | — | TrackMage 主仓库已从 GitHub 消失;AfterShip/17TRACK/快递100 为商业 SaaS→采购 API+自写 MCP 薄壳(~100 行) |
| 28 | 售后 | Chatwoot 客服工具链 | B | — | — | — | Chatwoot 可做售后客服台;退货流程需对接平台 API |
| 29 | 退款/退货 | 各平台官方 API(SP-API/Shopify/eBay) | — | — | — | — | 无独立开源退款引擎;对接平台 API 实现 |
| 30 | 销售数据分析 | **apache/superset** | **A** | 74.7k | **Apache-2.0** | Python | BI/报表,可嵌入,无 copyleft |
| 30 | 产品分析 | posthog/posthog | A | 39.7k | MIT 核心(+ee/) | Python+TS | 官方 MCP,转化漏斗/会话回放/Feature Flag |
| 30 | 流量分析 | umami-software/umami | A | 38.7k | MIT | TypeScript | 轻量隐私优先 Web 分析,部署极简 |
| 30 | 数据源(Amazon) | saleweaver/python-amazon-sp-api | A | 680 | MIT | Python | SP-API 封装,跨境销售分析核心数据源 |
| 31 | 财务/利润分析 | 自研 + InvenTree/Odoo 成本数据 | — | — | — | — | 利润计算无成熟开源;参考 CrossBorder-ERP-Lite 成本项口径;汇率自建 |
| 32 | AI Agent(多 Agent 编排) | crewAIInc/crewAI | A | 58.4k | MIT | Python | 角色协作多 Agent,内置 MCP 支持 |
| 32 | AI Agent(图编排) | langchain-ai/langgraph | A | 41.5k | MIT | Python | 图式多 Agent,状态/持久化/人审 |
| 32 | AI Agent(轻量) | openai/openai-agents-python | A | 29.4k | MIT | Python | 轻量 Agent Loop+Handoffs+Guardrails |
| 32 | AI Agent(Claude 原生) | anthropics/claude-agent-sdk-python | A | 8.1k | MIT | Python | Claude Agent SDK,原生 MCP client |
| 33 | MCP:浏览器自动化 | **microsoft/playwright-mcp** | **A** | 37.0k | Apache-2.0 | MCP | Microsoft **官方** MCP,无障碍树驱动,最适合电商后台表单 |
| 33 | MCP:浏览器(自主型) | browser-use/browser-use | A | 114.2k | MIT | Python | LLM 驱动浏览器 Agent,自带 MCP 模式 |
| 33 | MCP:Web Search | brave/brave-search-mcp-server | A | 1.4k | MIT | MCP | Brave **官方** Web Search MCP,需 API key |
| 33 | MCP:Web Search(零 key) | nickclyde/duckduckgo-mcp-server | A | 1.5k | MIT | MCP | 社区 DDG 搜索 MCP,零 key 即用 |
| 33 | MCP:GitHub | github/github-mcp-server(已配置) | A | 32.9k | MIT | Go | 本仓库已集成;搜索仓库/代码/Issue/PR |
| 34 | 浏览器自动化 | **microsoft/playwright** | B(底座) | 96.0k | Apache-2.0 | JS/Python | 底层框架;playwright-mcp 已覆盖 Agent 场景 |
| 34 | 浏览器自动化 | puppeteer/puppeteer | B(底座) | 95.6k | Apache-2.0 | JS | Chrome 底层库 |
| 35 | Web Search(自托管) | searxng/searxng | A | 36.8k | AGPL-3.0 | Python | 元搜索引擎,Docker 自托管,JSON API |
| 35 | Web Search(内容抓取) | **unclecode/crawl4ai** | **A** | 82.2k | **Apache-2.0** | Python | LLM 友好爬虫,许可最干净,可嵌入 |
| 35 | Web Search(全功能) | firecrawl/firecrawl | A | 179.1k | AGPL-3.0 | TypeScript | 网页→Markdown,官方 MCP;AGPL 注意 |
| 36 | 数据采集(价格监控) | **dgtlmoon/changedetection.io** | **A** | 33.8k | Apache-2.0 | Python | 网页/价格变更监控,Docker 自托管,REST+Webhook |
| 36 | 数据采集(爬虫) | scrapy/scrapy | B | 64.3k | BSD-3 | Python | 经典爬虫框架,适合结构化批量采集 |
| 36 | 数据采集(选品) | —(商业 SaaS 垄断) | — | — | — | — | Keepa/Helium10/Sorftime 全部付费;GitHub 壳项目(sorftime skill 850★)无自带数据 |
| 36 | 数据采集(1688) | ❌ MTOP 逆向库法律高危 | D | — | — | — | QuoVadis86/ai-reverse 等禁止生产使用;合规路径=open.1688.com ISV |

---

## 核心发现

### 1. 最值得直接集成的 5 个项目(完整版)

| # | 项目 | Stars | License | 覆盖模块 | 理由 |
|---|---|---|---|---|---|
| 1 | **medusajs/medusa** | 36.3k | MIT | 07商品 10发布 16订单 14库存 17支付 | 官方 MCP+Agent Skills,API-first,模块化,TypeScript,个人/小团队可维护 |
| 2 | **inventree/InvenTree** | 7.6k | MIT | 06供应商 07SKU 14库存 | 官方 MCP+Python SDK+官方 MCP 插件;同类唯一 MIT |
| 3 | **odoo/odoo Community** | 54.3k | LGPL-3.0 | 15采购 12成本 31财务 | 20 年成熟采购模块,已有 2 个高星 MCP(408★+384★);LGPL SaaS 友好 |
| 4 | **microsoft/playwright-mcp** | 37.0k | Apache-2.0 | 34浏览器 33MCP | 官方 MCP,确定性操作,最适合电商后台表单/Listings/后台自动化 |
| 5 | **chatwoot/chatwoot** | 36.7k | MIT 核心 | 19客服 28售后 | 全渠道(邮件/聊天/WhatsApp/FB/IG/Telegram)+REST+社区 MCP |

### 2. 最值得参考/抽取的 10 个项目

| # | 项目 | Stars | 参考价值 |
|---|---|---|---|
| 1 | **saleor/saleor** | 23.3k | BSD-3;GraphQL+schema 自描述对 Agent 友好;官方 MCP;多渠道多仓库设计 |
| 2 | **dgtlmoon/changedetection.io** | 33.8k | Apache-2.0;网页/价格变更监控,REST+Webhook,数据采集底座 |
| 3 | **apache/superset** | 74.7k | Apache-2.0;嵌入式 BI,可作为所有数据分析模块的统一看板 |
| 4 | **knadh/listmonk** | 23.4k | AGPL;Go 单二进制邮件营销,架构极简,Agent 工具化设计参考 |
| 5 | **twentyhq/twenty** | 56.6k | AGPL 核心+MIT SDK;GraphQL CRM,"为 AI 设计"的架构 |
| 6 | **crewAIInc/crewAI** | 58.4k | MIT;角色协作多 Agent,内置 MCP,适合业务多 Agent 编排 |
| 7 | **saleweaver/python-amazon-sp-api** | 680 | MIT;Amazon SP-API 全服务封装,issues 仅 2,数据接入层参考 |
| 8 | **unclecode/crawl4ai** | 82.2k | Apache-2.0;LLM 友好爬虫,许可最干净,商品数据采集核心工具 |
| 9 | **shopware/shopware** | 3.4k | MIT;官方 admin-mcp 现成,全功能商务平台参考 |
| 10 | **mautic/mautic** | 10.5k | GPL-3.0;全功能营销自动化引擎,campaign 流程设计参考 |

### 3. 开源真空(必须走 SaaS API 或自研)

| 领域 | 原因 |
|---|---|
| **物流追踪** | TrackMage 主仓库已从 GitHub 消失;所有候选≤10★;用 AfterShip/17TRACK SaaS+自写 MCP |
| **清关/税费** | VATComply 是纯 SaaS 无开源;VIES 官方 API 免费可自建工具;HS 归类用 LLM+公开表 |
| **选品/竞品数据** | Keepa/Helium10/JungleScout/Sorftime 全部商业 SaaS,GitHub 只有壳(Sorftime MCP 850★,无自带数据) |
| **关键词搜索量** | 唯一合规来源=Google Ads KeywordPlanIdeaService(需广告账户);pytrends 已归档 |
| **Amazon Repricer** | 开源生态已死(最高 5★);自研基于 Listings-Pricing API |
| **多渠道 Listing 同步** | GitHub 搜索结果 total=3,全部 0★,开源不存在;Sellbrite/ChannelAdvisor 为商业 SaaS |
| **Walmart SDK** | 最高 31★,无可用开源;走官方 OpenAPI 自生成 |
| **Temu 连接器** | 无任何开源;须走 partner.temu.com 官方申请后自研 |
| **1688/淘宝 SDK** | GitHub 无官方活跃 SDK;合规路径=ISV 签约;MTOP 逆向库法律高危禁止使用 |

---

## License 速查

| License | 自用(内部部署) | SaaS 给客户 | 传染性 | 典型案例 |
|---|---|---|---|---|
| MIT / Apache-2.0 | 自由 | 自由 | 无 | Medusa, InvenTree, Superset, Crawl4AI, Changedetection.io |
| BSD-3 | 自由 | 自由 | 无 | Saleor, Scrapy |
| LGPL-3.0 | 自由 | 自由(不改库源码) | 弱 | Odoo Community |
| GPL-3.0 | 自由 | 相对安全(无网络条款) | 中 | ERPNext, Mautic, Matomo |
| AGPL-3.0 | 自由 | 必须向用户提供完整源码 | 强 | Listmonk, LibreTranslate, Firecrawl, Twenty 核心 |
| Elastic License 2.0 | 自由 | ❌ 明确禁止提供托管服务 | — | OpenOMS |
| Unlicense | 完全自由 | 完全自由 | 无 | open-bsp-api |
| 仓库无 LICENSE 文件 | 不可商用 | 不可商用 | All Rights Reserved | CrossBorder-ERP-Lite |

**关键红线**:
- AGPL 项目 → 自用无碍,SaaS 必须开源修改
- Open Core 项目(Chatwoot/PostHog/Twenty/Metabase) → `enterprise/` 或 `ee/` 目录为商业许可,**部署时务必排除**
- "README 写着 MIT 但仓库无 LICENSE 文件" → 法律上不可商用

---

## 已核验"不存在/不可用/高风险"

| 项目 | 结论 |
|---|---|
| CrossBorder-ERP-Lite | 仓库无 LICENSE,法律上 All Rights Reserved,6 月停更 |
| OpenOMS | Elastic License 2.0,**非开源**,SaaS 明确违约 |
| OpenLinker | 36★/267 issues,alpha 阶段,比例异常 |
| pytrends | 已归档(2024-08),不可用于生产 |
| google-ads-python-lib | README 已改为"Ad Manager SOAP API",非 AdWords 关键词库 |
| Reaction Commerce | 官方声明"Project has been discontinued" |
| Shuup | 30 月无提交 |
| peppermint / parcelvoy / SEOstats | 已归档 |
| helpyio / sendportal | 停更 2~3 年 |
| stripe/stripe-mcp-server | **不存在**(API 404);Stripe 官方 MCP 实际在 stripe/ai |
| PayPal 官方 MCP | 12★,近一年无推送→停滞 |
| TrackMage | 主仓库已从 GitHub 删除 |
| vatcomply | **不存在**;VATComply 纯 SaaS |
| QuoVadis86/ai-reverse | 1688 MTOP 逆向 API+MCP,法律高危 |
| Amazon Repricer 开源 | 最高 5★,生态已死 |
| 多渠道 Listing 同步 | GitHub 0★,开源不存在 |
| Walmart SDK | 最高 31★,无可用开源 |

---

## 检索成本小结

5 组调研共花费 subagent ~2.2M tokens,覆盖 36 个模块,核验 ~120 个 GitHub 仓库。本轮发现的"开源真空"领域(物流追踪/清关/选品数据/repricer/多渠道同步)比"有成熟项目"的领域更有指导意义。**后续遵循本 skill 中的 Star 门槛规则,避免重复深挖低星项目。**

---

## 已配置的基础设施

| 工具 | 日期 | 用途 |
|---|---|---|
| github MCP(Remote+PAT,user 全局) | 2026-09-11 | GitHub 搜索 |
| claude-oracle-mcp(npx,user 全局) | 2026-09-11 | 15k+ MCP/skill/plugin 发现 |
| reuse-oss skill(references/) | 2026-09-11 | 候选评估工作流+检查清单 |
| ecomm-kb skill | 2026-09-11 | 本仓库知识蒸馏 |
| cross-border-capability-map skill(本文件) | 2026-09-12 | 36 模块开源能力地图 |

---

## 🏆 成果一:最值得直接集成的 5 个项目

| # | 项目 | Stars | License | 覆盖模块 | 理由 |
|---|---|---|---|---|---|
| 1 | **medusajs/medusa** | 36.3k | MIT | 商品·订单·库存·支付·发布 | 官方 MCP+Agent Skills+JS SDK,模块化,MIT 零法律摩擦,个人可维护 |
| 2 | **inventree/InvenTree** | 7.6k | MIT | 库存·SKU·供应商 | 同类唯一 MIT+官方 MCP+Python SDK,API-first;竞品全是 AGPL/GPL |
| 3 | **odoo/odoo Community** | 54.3k | LGPL-3.0 | 采购·成本·财务 | 20 年采购模块,已有 408★+384★ 两个 MCP;LGPL SaaS 友好 |
| 4 | **microsoft/playwright-mcp** | 37.0k | Apache-2.0 | 浏览器自动化·MCP | 官方 MCP,确定性操作,最适合电商后台批量操作(Listings/订单/表单) |
| 5 | **chatwoot/chatwoot** | 36.7k | MIT 核心 | 全渠道客服·售后 | 邮件+聊天+WhatsApp+FB+IG+Telegram,REST+3 个社区 MCP;避开 enterprise/ 即纯 MIT |

---

## 📚 成果二:最值得参考/抽取的 10 个项目

| # | 项目 | Stars | License | 参考价值 |
|---|---|---|---|---|
| 1 | **saleor/saleor** | 23.3k | BSD-3 | Python/Django+GraphQL+官方 MCP+多仓库多币种;schema 自描述 |
| 2 | **dgtlmoon/changedetection.io** | 33.8k | Apache-2.0 | Docker 自托管价格/网页变更监控,REST+Webhook,数据采集底座 |
| 3 | **apache/superset** | 74.7k | Apache-2.0 | 嵌入式 BI,所有数据分析模块的统一看板,零 copyleft |
| 4 | **knadh/listmonk** | 23.4k | AGPL-3.0 | Go 单二进制邮件营销,REST+社区 MCP;Agent 工具化最佳参考 |
| 5 | **twentyhq/twenty** | 56.6k | AGPL+MIT SDK | GraphQL CRM,"designed for AI",SDK MIT 可在外围闭源构建 Agent |
| 6 | **crewAIInc/crewAI** | 58.4k | MIT | 角色协作多 Agent,内置 MCP;业务多 Agent 编排首选 |
| 7 | **saleweaver/python-amazon-sp-api** | 680 | MIT | Amazon SP-API 全服务封装,issues 仅 2,当日仍推送 |
| 8 | **unclecode/crawl4ai** | 82.2k | Apache-2.0 | 同领域许可最干净的 LLM 友好爬虫,商品数据采集核心 |
| 9 | **shopware/shopware** | 3.4k | MIT | 全功能商务平台+官方 admin-mcp,Star 门槛达标且官方 MCP |
| 10 | **GeLi2001/shopify-mcp** | 238 | MIT | 现成 MCP server,完整示范"商业 API→Agent 工具"的封装模式 |

---

## 🏗 成果三:跨境电商 Agent 推荐架构与分阶段计划

### 推荐架构

```
┌─────────────────────────────────────────────┐
│           Claude Code (对话层)                │
│  自然语言指令 → AI Agent 拆解+执行             │
└──────────────────┬──────────────────────────┘
                   │ MCP 协议
┌──────────────────▼──────────────────────────┐
│         MCP Tool 层 (薄壳,~100行/个)          │
│  商品MCP→Medusa │ 订单MCP→Medusa              │
│  浏览器MCP→Playwright │ 搜索MCP→Brave/DDG     │
│  抓取MCP→Crawl4AI │ 客服MCP→Chatwoot         │
│  物流MCP→AfterShip │ 广告MCP→官方API          │
└──────────────────┬──────────────────────────┘
                   │ REST / GraphQL / SDK
┌──────────────────▼──────────────────────────┐
│         业务能力层 (自托管开源)                 │
│  Medusa(商品/订单/库存/支付)                   │
│  + InvenTree(库存深度) + Odoo Community(采购)  │
│  + Chatwoot(客服) + Listmonk+Postal(邮件)      │
│  + Superset(BI) + Umami(流量)                  │
│  + Changedetection.io(价格监控)                 │
│  [商业 SaaS:AfterShip(物流),Keepa(选品)]        │
└──────────────────────────────────────────────┘
```

**关键设计原则**:Agent → MCP 薄壳 → 业务 API → 数据库。Agent 不直接操作数据库,每层独立替换。

### 🥇 第一阶段:最小卖货闭环 (2-4 周)

**目标**:Agent 能帮你管理一个 Amazon 店铺。

| 做什么 | 怎么做 | 为什么 |
|---|---|---|
| 部署 Medusa | `npx create-medusa-app` | 商品+订单+库存+支付,MIT,30 分钟跑起来 |
| 接 Amazon SP-API | `pip install python-amazon-sp-api` | 680★,MIT,当日推送,靠谱 |
| 写 3 个 MCP Tool | 参考 GeLi2001/shopify-mcp | list_orders / get_inventory / update_listing,各 ~100 行 |
| 配 playwright-mcp | `claude mcp add playwright` | 后台批量操作(改价/回复消息/填表) |
| 配 changedetection.io | Docker 一键部署 | 竞品价格变动监控→告警喂给 Agent |
| ❌ 绝对不要碰 | ERPNext/Odoo 全量部署、自研订单引擎、1688 爬虫 | 太重/太慢/法律风险 |

**验收标准**:Agent 说出"库存 A 还有 120 件,竞品 B 昨天降价 $2,建议跟降 $1 并补货 200 件"。

### 🥈 第二阶段:多渠道+客服+数据 (4-8 周)

**目标**:多平台+有客服+能看数据。

| 做什么 | 怎么做 | 为什么 |
|---|---|---|
| 接 Shopify | GeLi2001/shopify-mcp(238★,MIT) | 现成 MCP,不写代码 |
| 接 eBay | YosefHayim/ebay-mcp(153★,MIT) | 现成 MCP |
| 接东南亚 | easycb/easycb-go(165★,MIT) | Go 库一拖四(Lazada/Shopee/TikTok/Shein) |
| 部署 Chatwoot | Docker | 全渠道客服台,对话直接喂 Agent |
| 部署 Superset | Docker | 所有平台订单/库存/广告一张看板 |
| 部署 Umami | Docker | 独立站流量分析 |
| 邮件能力 | Listmonk(Newsletter)+Postal(MTA) | 弃购召回/物流通知/促销 |
| ❌ 绝对不要碰 | Temu、Walmart、1688、自研多渠道同步、repricer | 无 SDK 或法律灰区或已死 |

**验收标准**:Agent 说出"Shopify 15 单 $890,eBay 8 单 $320,Amazon 32 单 $2,100,总和 $3,310,同比 +12%。3 条未回复消息已帮你回了。"

### 🥉 第三阶段:采购+供应链+利润 (8-16 周)

**目标**:采购降本+利润透明+多 Agent 协作。

| 做什么 | 怎么做 | 为什么 |
|---|---|---|
| 部署 Odoo Community | Docker Odoo + pip install mcp-odoo | 采购模块现成,不写 WMS/ERP |
| 写利润计算 MCP | 参考 CrossBorder-ERP-Lite 成本项 | Cost+运费+FBA+VAT+退货,纯计算最适合自研 |
| 接入 VIES/海关税率 | 自写 MCP 薄壳调官方 SOAP API | 免费合规 |
| 接入 AfterShip/17TRACK | 商业 API→自写 MCP(~100 行) | 物流追踪无开源,采购 API 唯一可行 |
| 多 Agent 编排 | CrewAI(58k★,MIT) | 选品/客服/采购/广告 Agent 角色协作 |
| SEO | crawlseo/crawlseo(582★,MIT,自带 MCP) | GSC 第一方 SEO 数据 Agent 可读 |
| Google Ads MCP | googleads/google-ads-mcp(933★,官方) | 广告数据+关键词规划师,零适配 |
| ❌ 绝对不要碰 | 自研 ERP/WMS、AGPL SaaS 转售、无 LICENSE 项目、1688 MTOP | 重资产/法律红线 |

**验收标准**:Agent 说出"综合净利润率 22.3%,比上月 +1.2%。采购成本可压缩 8%(供应商 A 比 B 贵 15%)。建议换供应商(需 ISV 签约)。"

### 绝对不要碰(总结)

| 类型 | 例子 | 原因 |
|---|---|---|
| GPL/AGPL 做 SaaS | ERPNext/Listmonk/SuiteCRM | 自用无碍,对外 SaaS 必须开源修改 |
| Elastic License/无 LICENSE | OpenOMS/CrossBorder-ERP-Lite | 法律不可商用 |
| 逆向/爬虫 API | 1688 MTOP/Temu 逆向库 | 违反平台协议+法律风险 |
| 已归档/停更 | Shuup/Reaction Commerce/pytrends/Helpy | 踩坑+没人修 |
| 生态已死 | Amazon Repricer/多渠道 Listing 同步 | 开源不存在,自研或买 SaaS |
| 自研重型系统 | 订单引擎/WMS/ERP | Medusa+InvenTree+Odoo 加起来比你写快 100 倍 |
| 选品数据开源替代 | 试图找免费 Ahrefs | Keepa API $20/月远比自己爬便宜 |

> **核心原则:用尽可能少的代码和尽可能多的成熟开源能力,快速跑通卖货→多渠道→提利润的闭环。**