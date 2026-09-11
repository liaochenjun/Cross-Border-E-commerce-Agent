# Cross-Border E-commerce Agent System Architecture

## 1. 系统最终目标

本项目最终建设一个真正可执行跨境电商业务的 AI Agent 系统。

用户不需要分别操作：

* 市场调研工具
* 选品工具
* 供应商工具
* ERP
* 邮箱
* 客服
* 物流
* 数据分析工具

而是向系统提出一个**商业目标**：

> “帮我测试日本老年防滑鞋这个产品。”

系统自动完成：

```text
商业目标
↓
任务拆解
↓
市场调研
↓
竞品分析
↓
产品筛选
↓
供应商搜索
↓
采购成本
↓
物流成本
↓
平台成本
↓
利润计算
↓
产品创建
↓
上架
↓
营销
↓
订单
↓
采购
↓
物流
↓
客服
↓
售后
↓
数据分析
↓
优化
```

最终形成：

> **从发现机会到产生订单，再到复盘优化的完整商业闭环。**

---

# 2. 总体架构

```text
                         用户
                          │
                          ↓
                  ┌───────────────┐
                  │   主 Agent    │
                  │  Orchestrator │
                  └───────┬───────┘
                          │
                ┌─────────┼─────────┐
                ↓         ↓         ↓
             Planner   Memory    Policy
                │
                ↓
        ┌─────────────────────┐
        │   Business Agents   │
        └──────────┬──────────┘
                   │
 ┌─────────────────┼─────────────────────┐
 ↓                 ↓                     ↓
Research        Product               Supplier
Agent           Agent                 Agent
 ↓                 ↓                     ↓
Market          SKU                  1688
Competitor      Pricing              Supplier
Keyword         Content              Procurement
 ↓                 ↓                     ↓
 └─────────────────┼─────────────────────┘
                   ↓
          ┌───────────────────┐
          │ Commerce Core     │
          │                   │
          │ Product           │
          │ SKU               │
          │ Inventory         │
          │ Order             │
          │ Customer          │
          └─────────┬─────────┘
                    │
       ┌────────────┼─────────────┐
       ↓            ↓             ↓
   Sales Agent  Operations     Customer
       │          Agent          Agent
       ↓            ↓             ↓
  Marketplace   Procurement    Customer Service
  Store         Inventory      Email
  Listing       Logistics      After-sales
       │            │             │
       └────────────┼─────────────┘
                    ↓
              Data / Analytics
                    │
                    ↓
              Agent Memory
                    │
                    └────────→ 主 Agent
```

---

# 3. 核心设计：一个主 Agent + 多个业务 Agent

不要让一个 Agent 直接承担所有事情。

采用：

```text
                    Main Agent
                        │
        ┌───────────────┼────────────────┐
        ↓               ↓                ↓
   Research Agent   Product Agent   Supplier Agent
        ↓               ↓                ↓
   Market Data       Product Data     Supplier Data
        │               │                │
        └───────────────┼────────────────┘
                        ↓
                  Operations Agent
                        │
             ┌──────────┼──────────┐
             ↓          ↓          ↓
         Sales       Order      Customer
         Agent       Agent       Agent
```

主 Agent 不负责具体业务细节。

它负责：

* 理解用户目标
* 创建任务计划
* 分配任务
* 调用业务 Agent
* 汇总结果
* 判断下一步
* 处理异常
* 请求人工确认

---

# 4. Main Agent

Main Agent 是整个系统的大脑。

核心流程：

```text
User Goal
↓
Goal Understanding
↓
Task Planning
↓
Agent Selection
↓
Task Execution
↓
Result Evaluation
↓
Next Task
↓
Final Decision
```

例如：

```text
用户：

帮我测试日本老年防滑鞋。

Main Agent：

创建项目
↓
Research Agent
↓
Product Agent
↓
Supplier Agent
↓
Cost Agent
↓
Decision
↓
Human Approval
↓
Listing Agent
↓
Sales Agent
```

---

# 5. Business Agent

系统按照业务领域拆分 Agent。

## 5.1 Research Agent

负责：

```text
市场规模
市场趋势
关键词
消费者需求
竞品
品牌
价格
评价
差评
产品卖点
市场空白
```

输出标准化：

```json
{
  "market": "...",
  "demand": "...",
  "competitors": [],
  "price_range": {},
  "customer_pain_points": [],
  "opportunities": []
}
```

---

# 6. Product Agent

负责：

```text
选品
SKU
规格
产品属性
产品图片
产品描述
产品卖点
产品内容
产品翻译
产品定价
```

输入：

```text
市场需求
+
竞品
+
供应商数据
```

输出：

```text
候选产品
↓
评分
↓
推荐产品
```

---

# 7. Supplier Agent

负责：

```text
供应商搜索
供应商比较
采购价格
MOQ
SKU
供货能力
供应商评分
历史价格
```

核心：

```text
Supplier
Supplier Product
Supplier SKU
Purchase Price
MOQ
Lead Time
Supplier Score
```

---

# 8. Cost Agent

成本必须独立。

不要让 LLM 自己随意算钱。

系统使用确定性计算引擎：

```text
采购成本
+
国内物流
+
国际物流
+
平台费用
+
支付费用
+
税费
+
广告成本
+
退货成本
+
其他成本
=
Total Cost
```

然后：

```text
Selling Price
-
Total Cost
=
Profit
```

Agent 负责解释和决策。

计算引擎负责计算。

---

# 9. Decision Agent

这是商业价值非常高的一层。

它负责判断：

```text
值得不值得做
值得不值得采购
哪个供应商更好
哪个 SKU 更好
卖多少钱
预计利润
风险多大
是否开始测试
是否扩大采购
是否停止产品
```

例如：

```text
候选产品 A
利润率 31%
需求高
竞争中等
供应稳定

→ 推荐测试
```

---

# 10. Commerce Core

Commerce Core 是系统的业务基础。

负责：

```text
Product
SKU
Price
Inventory
Order
Customer
```

Agent 不直接修改数据库。

统一：

```text
Agent
↓
Business API / MCP
↓
Commerce Core
↓
Database
```

这样以后替换 Commerce Core 不会影响 Agent。

---

# 11. Inventory Agent

负责：

```text
库存监控
库存预测
安全库存
缺货预警
补货建议
库存同步
```

例如：

```text
当前库存：32

过去 7 天销量：21

预计 5 天后缺货

→ 生成补货任务
```

但采购行为默认需要人工确认。

---

# 12. Procurement Agent

负责：

```text
供应商选择
采购数量
采购价格
采购订单
采购进度
到货
异常
```

流程：

```text
库存不足
↓
Inventory Agent
↓
Procurement Agent
↓
查询供应商
↓
比较价格
↓
生成采购方案
↓
Human Approval
↓
采购
```

---

# 13. Sales Agent

负责销售渠道。

统一抽象：

```text
Channel Adapter
```

例如：

```text
Amazon
Shopify
eBay
TikTok Shop
独立站
```

Sales Agent 不应该绑定某个平台。

统一：

```text
Sales Agent
↓
Channel API
↓
Marketplace
```

核心能力：

```text
创建 Listing
修改 Listing
同步价格
同步库存
同步订单
获取销售数据
```

---

# 14. Listing Agent

负责：

```text
标题
描述
Bullet Points
关键词
图片
翻译
SEO
价格
SKU
库存
```

流程：

```text
Product Data
↓
Listing Agent
↓
生成平台内容
↓
Human Review
↓
Publish
```

---

# 15. Order Agent

负责：

```text
订单获取
订单状态
付款状态
库存扣减
采购触发
发货触发
物流状态
订单异常
```

完整流程：

```text
Customer Order
↓
Order Agent
↓
库存检查
↓
Inventory
↓
缺货？
├── No → Fulfillment
└── Yes → Procurement
```

---

# 16. Logistics Agent

负责：

```text
物流渠道
运费
发货
Tracking
物流状态
异常物流
签收
```

流程：

```text
Order
↓
Logistics Agent
↓
选择物流方案
↓
创建 Shipment
↓
Tracking
↓
持续监控
```

---

# 17. Customer Agent

负责：

```text
客户消息
订单查询
物流查询
产品咨询
售后
退款
退货
投诉
```

流程：

```text
Customer Message
↓
Customer Agent
↓
识别意图
↓
查询订单/物流/产品
↓
生成答案
↓
高风险？
├── No → 自动回复
└── Yes → Human Review
```

---

# 18. Marketing Agent

负责：

```text
SEO
广告
内容
邮件
促销
社媒
```

核心循环：

```text
Traffic
↓
Conversion
↓
Sales
↓
Profit
↓
Analysis
↓
Marketing Adjustment
```

---

# 19. Analytics Agent

负责整个商业数据分析。

输入：

```text
Sales
Orders
Products
Traffic
Ads
Costs
Profit
Customers
Returns
```

输出：

```text
销售趋势
利润趋势
爆款
滞销
广告 ROI
客户价值
产品利润
渠道利润
供应商利润
```

---

# 20. Finance Agent

负责：

```text
收入
成本
平台费用
支付费用
物流费用
税费
广告费用
退款
利润
现金流
```

核心：

```text
Revenue
-
COGS
-
Logistics
-
Platform Fee
-
Payment Fee
-
Ads
-
Tax
-
Returns
=
Net Profit
```

---

# 21. MCP 层

MCP 不属于业务逻辑。

MCP 是 Agent 与外部能力之间的连接层。

```text
Business Agent
↓
MCP Tool
↓
Adapter
↓
External Service
```

例如：

```text
Research Agent
↓
search_web
↓
Search API

Supplier Agent
↓
search_1688_products
↓
1688 Adapter

Order Agent
↓
get_orders
↓
Amazon Adapter

Customer Agent
↓
get_customer_messages
↓
Chatwoot
```

---

# 22. Adapter 层

每一个外部平台建立 Adapter。

例如：

```text
adapters/
├── 1688/
├── amazon/
├── shopify/
├── ebay/
├── logistics/
├── payment/
└── email/
```

Adapter 负责：

* API
* 数据转换
* 鉴权
* 错误处理
* 限流
* 重试
* 缓存

业务 Agent 不处理第三方 API 细节。

---

# 23. Data Architecture

数据库按照业务域设计。

核心实体：

```text
User
Business
Project

Product
SKU
Category

Supplier
SupplierProduct
SupplierSKU

Inventory
Warehouse

Order
OrderItem

Customer

Shipment
Tracking

Payment

Cost
Profit

Marketing
Campaign

MarketResearch
Competitor
Keyword

AgentTask
AgentExecution
ToolCall
```

---

# 24. Business Project

系统必须有“项目”概念。

例如：

```text
Project:
日本老年防滑鞋
```

这个项目下面关联：

```text
Market Research
Products
Competitors
Suppliers
Costs
Listings
Orders
Customers
Profit
```

这样 Agent 才能长期围绕一个商业项目工作。

---

# 25. Agent Task System

所有 Agent 工作都转化成 Task。

```text
Task
├── id
├── project_id
├── type
├── status
├── priority
├── input
├── output
├── assigned_agent
├── created_at
└── completed_at
```

状态：

```text
PENDING
RUNNING
WAITING
SUCCESS
FAILED
CANCELLED
HUMAN_REVIEW
```

---

# 26. Event Driven Architecture

Agent 不应该一直轮询。

业务发生事件：

```text
OrderCreated
PaymentReceived
InventoryLow
ShipmentDelayed
CustomerMessageReceived
ProductPriceChanged
SupplierPriceChanged
```

触发：

```text
Event
↓
Agent
↓
Task
↓
Action
```

例如：

```text
InventoryLow
↓
Procurement Agent
↓
Check Supplier
↓
Create Purchase Recommendation
↓
Human Approval
```

---

# 27. Memory Architecture

Agent Memory 分成三层。

## Short-term Memory

当前任务：

```text
当前目标
当前计划
当前 Tool Call
当前结果
```

## Business Memory

长期业务数据：

```text
产品
供应商
订单
客户
利润
```

## Knowledge Memory

长期知识：

```text
市场知识
产品知识
平台规则
运营经验
历史分析
```

三者不能混为一谈。

---

# 28. Human Approval Layer

高风险动作必须经过人工。

```text
低风险
Search
Read
Analyze
Generate Draft

↓

中风险
Create Listing Draft
Change Price
Inventory Adjustment

↓

高风险
Publish
Purchase
Payment
Refund
Delete
Account Change
```

高风险：

```text
Agent
↓
Approval Request
↓
Human
↓
Approve / Reject
↓
Execute
```

---

# 29. Security Layer

统一管理：

```text
API Key
OAuth Token
Cookies
Platform Credentials
Database Credentials
```

所有 Secret：

```text
Environment Variables
+
Secret Manager
```

禁止：

```text
写死代码
提交 Git
写入日志
暴露给 Agent
```

Agent 只能获得完成当前任务所需要的最小权限。

---

# 30. Observability

整个系统必须可以看到：

```text
Agent Task
↓
Plan
↓
Agent
↓
Tool
↓
API
↓
Result
↓
Decision
↓
Action
```

记录：

```text
耗时
Token
工具调用
错误
重试
成本
人工介入
最终结果
```

这样以后才能知道：

> 到底是 Agent 不行，工具不行，还是数据不行。

---

# 31. 最终业务闭环

最终系统必须形成：

```text
                  ┌──────────────┐
                  │ Market       │
                  │ Opportunity  │
                  └──────┬───────┘
                         ↓
                    Product
                         ↓
                    Supplier
                         ↓
                  Cost / Profit
                         ↓
                     Decision
                         ↓
                    Listing
                         ↓
                    Marketing
                         ↓
                      Order
                         ↓
                   Procurement
                         ↓
                    Fulfillment
                         ↓
                    Logistics
                         ↓
                    Customer
                         ↓
                   After-sales
                         ↓
                    Analytics
                         ↓
                    Profit
                         ↓
                  Optimization
                         │
                         └──────────→ Market
```

这才是系统最终的“挣钱机器”。

---

# 32. 第一阶段实现边界

虽然最终架构很大，但开发必须按照业务闭环逐步扩展。

第一条真正可运行链路：

```text
用户
↓
Main Agent
↓
Research Agent
↓
Search
↓
Browser
↓
Crawler
↓
Market Data
↓
Product Agent
↓
候选产品
```

第二条：

```text
候选产品
↓
Supplier Agent
↓
1688
↓
供应商
↓
采购价格
```

第三条：

```text
供应商
↓
Cost Agent
↓
物流 / 平台 / 支付成本
↓
Profit Agent
↓
是否值得测试
```

第四条：

```text
确定测试
↓
Commerce Core
↓
Product
↓
SKU
↓
Inventory
↓
Listing
```

第五条：

```text
Listing
↓
Sales Channel
↓
Order
↓
Procurement
↓
Logistics
↓
Customer Service
↓
Profit
```

---

# 33. 最终系统形态

最终用户看到的应该不是：

> “请选择 MCP。”

而是：

```text
用户：

我想测试日本老年防滑鞋。

Agent：

正在分析。

[市场]
日本老年鞋市场需求……

[竞品]
发现 27 个主要竞品……

[供应商]
发现 14 个供应商……

[成本]
预计总成本 ¥……

[利润]
预计毛利率 32.4%……

[建议]
推荐测试 3 个 SKU。

是否进入产品创建阶段？
```

用户确认：

```text
进入。
```

然后：

```text
Agent
↓
创建 Product
↓
创建 SKU
↓
设置价格
↓
设置库存
↓
生成 Listing
↓
等待发布确认
```

产生订单以后：

```text
Order
↓
库存
↓
采购
↓
物流
↓
客服
↓
售后
↓
利润
↓
分析
```

用户最终只需要处理：

> **钱、风险、战略和关键审批。**

---

# 34. 架构最高原则

整个项目始终遵守：

> **Agent 是大脑，MCP 是接口，Adapter 是翻译层，Business Core 是业务执行系统，Database 是事实来源，Event 是触发机制，Human Approval 是风险边界。**

不要把所有逻辑塞进 Agent。

不要把业务逻辑塞进 MCP。

不要让第三方平台 API 直接污染业务层。

不要让 LLM 负责确定性计算。

不要让 Agent 在没有权限控制的情况下执行高风险商业操作。

最终目标：

> **不是做一个“会聊天的跨境电商 AI”，而是做一个能够持续运行跨境电商业务流程的 Agent Operating System。**
