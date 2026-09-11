---
name: ecomm-kb
description: 跨境电商知识库仓库 (ecomm) 的蒸馏知识。当需要在本仓库新增/整理模块文档、维护 clash/config.yaml 或 ax6000.md、回答本项目结构/网络环境/贡献与版权规范相关问题,或了解路由器透明代理与 Clash 配置模板时使用。
---

# 跨境电商知识库 · 项目蒸馏

> 本 skill 是仓库核心知识的蒸馏版,供后续会话快速进入上下文。细节仍以仓库原文件为准。

## 1. 项目定位与规范

- 开源跨境电商(出海)知识库,服务中国卖家,覆盖技术环境、平台运营、独立站、供应链、物流、合规风控全链路。
- 定位是"学习参考",不构成法律/税务/投资建议;网络技术仅用于跨境运营的合法合规需求(访问后台、海外社媒营销)。
- 协议 **CC BY-NC-SA 4.0**:转载须署名;禁止打包售卖或付费培训;衍生作品须同协议。
- 贡献流程:Fork → 新建 `Feat_xxx` 分支 → 提交 → PR。

## 2. 实际文件 vs 规划结构

README 规划了 00-09 十个模块目录,但**目前尚未创建**。仓库实际文件只有:

- `README.md` — 总导航、模块规划、贡献与免责声明
- `ax6000.md` — Redmi AX6000 路由器 + ShellCrash 环境笔记
- `clash/config.yaml` — 路由端 Clash 配置模板

规划模块(新增内容时按此编号组织):

| 目录 | 主题 | 要点 |
|---|---|---|
| `00-ReadMe` | 导航 | 新手路线图、术语表(SKU/ASIN/ROI/VAT)、贡献指南 |
| `01-Infrastructure` | 网络与环境 | 节点/专线、防关联(指纹浏览器 AdsPower/紫鸟、住宅/机房 IP)、多账号硬件隔离 |
| `02-Compliance` | 主体与合规 | 大陆/香港/美国公司注册、欧洲 VAT、美国 Sales Tax、商标/品牌备案、FCC/CE/UL/CPC/FDA |
| `03-Platforms` | 平台与独立站 | Amazon(FBA/FBM、二审、视频验证)、TikTok Shop、Walmart/Temu/SHEIN/Etsy/eBay/Shopee;独立站 Shopify/WooCommerce/Shopline;支付 PayPal/Stripe/2Checkout |
| `04-SupplyChain` | 供应链选品 | 数据选品(Helium 10/JS)、1688/广交会/产业带、定价与利润计算 |
| `05-Logistics` | 物流仓储 | 头程(海运/空派/中欧班列)、清关、尾程;FBA/第三方海外仓/虚拟仓;FOB/CIF/DDP/EXW |
| `06-Marketing` | 运营推广 | Listing SEO、Amazon PPC(SP/SB/SD)、FB/IG Ads、Google SEM、TikTok/网红/Deal 站 |
| `07-Tools` | 工具栈 | ERP(店小秘/马帮/积加/领星)、AIGC 提效、GA4 |
| `08-RiskManagement` | 风控 | 账号申诉(POA 撰写)、赶跟卖、恶意差评应对 |
| `09-Management` | 组织管理 | 团队架构、KPI/OKR、客服 SOP |

## 3. 网络环境 (ax6000.md 蒸馏)

- **设备**:Redmi AX6000 — MTK Filogic 830 四核 2GHz、512MB RAM、160MHz 频宽、8 数据流、8 路信号放大器;4 个自适应千兆口,支持 LAN 聚合与 Mesh。
- **SSH**:固件 1.0.67 下可行,步骤见 right.com.cn 论坛 thread-8253125;OpenWrt 端公钥放 `/etc/dropbear/authorized_keys`。
- **ShellCrash** (juewuy/ShellCrash) 安装与配置:

  ```shell
  sh -c "$(curl -kfsSl https://fastly.jsdelivr.net/gh/juewuy/ShellCrash@master/install.sh)" && source /etc/profile &> /dev/null
  ```

  关键选项:稳定版;安装到 `/data`;局域网透明代理(启用);软固化选 0(已固化);安装源切 **Cloudflare_CDN**(快);防火墙改**混合模式**;用 providers 方式生成配置(模板选"极简",或直接用本仓库 `clash/config.yaml`);启用**域名嗅探**;Dashboard 装 **Yacd-Meta** 到 `/data/ShellCrash/ui`,访问 `http://192.168.12.1:9999/ui`。

## 4. Clash 配置模板要点 (clash/config.yaml)

- **端口**:`mixed-port: 7890`、`redir-port: 7892`、`tproxy-port: 7893`、`external-controller: :9999`。
- **DNS**:fake-ip 模式(`198.18.0.1/16`),监听 `:1053`;default-nameserver 用 114.114.114.114 / 223.5.5.5;nameserver/fallback 用 DoH(阿里 223.5.5.5、doh.pub、rubyfish tls);fake-ip-filter 覆盖国内音乐/游戏/CDN/NTP 等大量域名,保证国内流量不被 fake-ip 污染。
- **节点**:两个 http 型 proxy-provider `Singapore-A` / `Japan-TK3`,**url 是占位符,须替换为自己的订阅地址**;健康检查用 `https://www.gstatic.com/generate_204`;override 开 `udp` + `skip-cert-verify`;分组为 Selection/Final(select)+ 按节点的 url-test。
- **规则**:静态规则只有三条(`LAN → DIRECT`、`GEOIP CN → Direct`、`MATCH → Final`),实际分流靠 `script:` 里的 `main(ctx, metadata)`:QUIC UDP 443 先 REJECT → 非常见端口 DIRECT → 按规则集优先级匹配(Special/流媒体/Telegram/OpenAI 等)→ GeoIP CN → Others。
- **rule-providers**:全部走 dler-io/Rules 仓库,经 `gl.bbkss.org` 反代,如 `https://gl.bbkss.org/https://raw.githubusercontent.com/dler-io/Rules/main/Clash/Provider/{名称}.yaml`;媒体类在 `Provider/Media/` 子目录,含 Netflix/YouTube/Disney Plus/Bilibili/腾讯视频/优酷 等。
- ⚠️ `tun`/`experimental` 段(utun、en0)是旧 Mac 配置残留,路由器上实际走 tproxy 模式,改配置时不要照搬这两段。
