# Nexus AI 应用开发工程师实习训练计划

## W1 详细计划：Prompt 基础 + OpenAI API 环境搭建

**周期**：第 1 周  
**推荐投入**：20 - 28 小时  
**阶段定位**：夯实 AI 应用开发基础

## 1. 本周定位

W1 是整个三个月计划的起点，目标不是堆技术，而是建立 AI 应用开发的最小闭环：能够理解 Prompt 的基本设计方法，完成 OpenAI / Claude / 国产大模型 API 的调用环境，并用 FastAPI 封装一个可运行的 AI 服务原型。该周成果将作为 Nexus Research、Nexus Dev、Nexus Agent 三个项目的公共技术底座。

| 本周主题 | 核心能力 | 产出物 | 验收标准 |
| --- | --- | --- | --- |
| Prompt + API | 结构化输出、Function Calling、Streaming、FastAPI 封装 | 一个 AI Assistant API 原型 + Prompt 笔记 + GitHub README | 可以本地运行、可复现、可展示、代码结构清晰 |

## 2. 本周学习目标

- 理解 Prompt Engineering 的核心范式：角色设定、任务拆解、输入约束、输出格式、Few-shot、错误修正。
- 掌握 LLM API 的基本调用方式：Chat Completion、Streaming、Structured Output、Function Calling / Tool Calling。
- 用 Python 构建一个最小 AI 服务：FastAPI + Pydantic + 环境变量管理 + 简单错误处理。
- 形成可写入简历和项目文档的工程化习惯：README、运行截图、接口文档、开发日志。
- 为 Nexus 三大项目沉淀通用组件：模型调用封装、Prompt 模板、配置管理、基础接口。

## 3. 每日执行计划

### D1 - D4：从 Prompt 到模型调用封装

| Day | 主题 | 学习任务 | 实践任务 | 当天交付 |
| --- | --- | --- | --- | --- |
| D1 | 定位与环境搭建 | 明确 AI 应用开发工程师能力模型；配置 Python、虚拟环境、API Key、Git 仓库。 | 创建 `nexus-ai-lab` 仓库；建立 `/apps`、`/packages`、`/prompts`、`/docs` 目录。 | 环境截图 + README 初版 |
| D2 | Prompt 基础 | 学习角色设定、任务边界、输入输出约束、Few-shot 示例。 | 为“行业信息总结”“代码解释”“任务拆解”分别写 3 组 Prompt。 | Prompt 模板 9 个 |
| D3 | 结构化输出 | 学习 JSON Schema、Pydantic、稳定结构化输出、异常输出修复。 | 实现 summary / classify / extract 三类结构化输出函数。 | `structured_output.py` |
| D4 | LLM API 调用 | 学习 Chat、Streaming、温度参数、上下文组织、模型调用封装。 | 封装 ModelClient，支持普通输出与流式输出。 | `model_client.py` |

### D5 - D7：从工具调用到 FastAPI Demo 与复盘

| Day | 主题 | 学习任务 | 实践任务 | 当天交付 |
| --- | --- | --- | --- | --- |
| D5 | Function Calling | 理解 Tool Calling 思想：模型负责决策，工具负责执行。 | 实现 2 个工具：网页摘要占位工具、任务清单生成工具。 | `tools.py` + 调用示例 |
| D6 | FastAPI AI 服务 | 学习 FastAPI 路由、Pydantic 请求响应、异常处理。 | 封装 `/chat`、`/summarize`、`/plan` 三个接口。 | 可运行 API Demo |
| D7 | 复盘与包装 | 整理本周能力、问题、下一周计划。 | 补充 README、录制 1 分钟 Demo、写一篇学习日志。 | 周总结 + Demo 链接 |

## 4. 本周最小项目：Nexus Base Assistant

本周不直接启动完整三大项目，而是先做一个公共底座项目：Nexus Base Assistant。它是后续 Nexus Research、Nexus Dev、Nexus Agent 的通用 AI 能力层。

| 模块 | 功能 | 后续复用方向 |
| --- | --- | --- |
| Prompt Library | 沉淀可复用 Prompt 模板 | Nexus Research 报告生成、Nexus Dev Code Review、Nexus Agent 任务拆解 |
| Model Client | 统一封装 LLM 调用 | 所有项目共用模型访问层 |
| Tool Calling Demo | 实现工具调用原型 | 为 Agent 工具生态打基础 |
| FastAPI Service | 提供 AI API 接口 | 后续接前端、部署、Demo 展示 |

## 5. 与 Nexus 三大项目的关系

| 项目 | W1 支撑点 | 后续扩展 | 产品意识训练 |
| --- | --- | --- | --- |
| Nexus Research | 摘要、分类、信息抽取 Prompt | RAG 检索、报告生成、可信引用 | 把“文档问答”包装为“行业研究工作流” |
| Nexus Dev | 代码解释 Prompt、API 封装 | 代码 RAG、Review Agent、PR 生成 | 把“代码助手”包装为“研发协作平台” |
| Nexus Agent | 任务拆解 Prompt、Tool Calling 原型 | LangGraph、多 Agent、MCP | 把“Agent Demo”包装为“任务编排系统” |

## 6. 学习资源建议

- OpenAI Cookbook：重点看 structured outputs、tool calling、streaming 相关示例。
- Prompt Engineering Guide：重点看 prompt patterns、few-shot、structured prompting。
- FastAPI 官方文档：重点看 Path Operation、Pydantic Models、Error Handling。
- Pydantic 文档：重点看 BaseModel、Field、类型校验、JSON Schema。
- 任选一个国产模型平台作为备用：DeepSeek、通义千问、智谱 GLM，用于增强简历中的多模型适配能力。

## 7. 本周交付清单

- [ ] GitHub 仓库：`nexus-ai-lab`，包含清晰 README 和运行方式。
- [ ] Prompt 模板库：至少 9 个 Prompt，覆盖总结、抽取、分类、任务拆解、代码解释。
- [ ] 模型调用封装：ModelClient 支持普通调用、流式输出、异常处理。
- [ ] FastAPI Demo：提供 `/chat`、`/summarize`、`/plan` 三个接口。
- [ ] 开发日志：记录每天学到的内容、遇到的问题和解决方案。
- [ ] Demo 素材：至少 3 张截图或 1 分钟录屏，为后续简历和面试准备素材。

## 8. 验收标准与自评表

| 维度 | 优秀 | 合格 | 需要改进 |
| --- | --- | --- | --- |
| Prompt 能力 | 输出稳定、有结构、有边界条件 | 能完成基本任务 | 输出不稳定，依赖反复追问 |
| API 能力 | 封装清晰，支持错误处理和流式输出 | 能正常调用模型 | 代码散乱，难以复用 |
| 工程习惯 | README 完整，目录清晰，可一键运行 | 能本地运行 | 缺少文档或运行说明 |
| 产品意识 | 能说明该能力如何支撑 Nexus 三大项目 | 能说明基本用途 | 只停留在技术点描述 |

## 9. 本周时间分配建议

| 类型 | 建议时长 | 说明 |
| --- | --- | --- |
| 学习 | 8 - 10 小时 | 阅读文档、理解 Prompt / API / FastAPI 核心概念 |
| 编码 | 8 - 12 小时 | 完成 ModelClient、Prompt Library、FastAPI Demo |
| 整理 | 3 - 4 小时 | README、开发日志、截图、Demo 录制 |
| 复盘 | 1 - 2 小时 | 总结问题并制定 W2 计划 |

## 10. W1 结束后应具备的表达方式

面试或简历中，你可以这样描述本周成果：

> 完成 Nexus AI 应用底座搭建，封装统一 LLM 调用层和 Prompt 模板库，基于 FastAPI 实现支持结构化输出、流式响应和工具调用原型的 AI Assistant 服务，为后续 RAG、Code Agent 和 Multi-Agent Workflow 项目提供公共能力。
