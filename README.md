# Nexus AI Lab

Nexus AI Lab 是 AI 应用开发工程师实习训练项目的公共技术底座，用于沉淀 Prompt 模板、模型调用封装、结构化输出、工具调用示例和 FastAPI AI 服务。

本项目将作为后续三个 Nexus 项目的公共能力层：

- Nexus Research：AI 行业研究与情报分析平台
- Nexus Dev：AI 代码理解与研发协作平台
- Nexus Agent：多智能体任务编排平台

## 项目定位

本项目的目标不是训练大模型，而是学习如何将大模型能力集成到真实应用中，形成可复用、可运行、可展示的 AI 应用开发能力。

核心训练内容包括：

- Prompt Engineering
- LLM API 调用封装
- Structured Output
- Function Calling / Tool Calling
- FastAPI AI 服务封装
- 项目文档、开发日志与 Demo 展示

## W1 学习目标

- 理解 Prompt Engineering 的核心范式：角色设定、任务拆解、输入约束、输出格式、Few-shot、错误修正
- 掌握 LLM API 的基本调用方式：Chat、Streaming、Structured Output、Function Calling / Tool Calling
- 使用 Python 构建最小 AI 服务：FastAPI + Pydantic + 环境变量管理 + 简单错误处理
- 形成工程化习惯：README、运行截图、接口文档、开发日志
- 为 Nexus 三大项目沉淀通用组件：模型调用封装、Prompt 模板、配置管理、基础接口

## 项目结构

```text
Nexus/
├── apps/                         应用入口，例如 FastAPI 服务
├── packages/                     可复用代码模块
│   ├── __init__.py
│   ├── model_client.py           统一 LLM API 调用封装
│   └── structured_output.py      结构化输出模型与校验
├── prompts/                      Prompt 模板库
│   ├── research/                 Nexus Research 相关 Prompt
│   ├── dev/                      Nexus Dev 相关 Prompt
│   └── agent/                    Nexus Agent 相关 Prompt
├── tests/                        API 测试脚本
│   ├── prompt_api_tests.py
│   └── structured_output_api_test.py
├── docs/                         项目文档
│   ├── plans/                    实习计划、周计划、路线图等规划类文档
│   ├── logs/                     每日开发日志
│   ├── notes/                    学习笔记与测试记录
│   ├── images/                   环境截图、接口截图、运行截图
│   └── demos/                    Demo 说明、录屏链接、展示素材
├── .python-version               uv 固定的 Python 版本
├── .gitignore                    Git 忽略规则
├── README.md                     项目说明文档
└── requirements.txt              Python 依赖列表
```

## 文档说明

- `docs/plans/`：项目规划文档，使用 Markdown 格式方便 GitHub 在线阅读
- `docs/logs/`：每日开发日志，记录每日目标、完成内容、问题与复盘
- `docs/notes/`：学习笔记、Prompt 测试记录、结构化输出测试记录
- `docs/images/`：环境截图、运行截图、接口截图
- `docs/demos/`：Demo 说明、录屏链接、展示素材
- `prompts/`：Prompt 模板库，按 Research、Dev、Agent 三类能力组织
- `packages/`：可复用 Python 模块，例如模型调用封装、结构化输出模型
- `tests/`：API 测试脚本，用于验证 Prompt、ModelClient 和结构化输出能力

## 环境准备

本项目使用 `uv` 管理 Python 版本和虚拟环境。

### 创建环境

```powershell
uv python pin 3.11
uv venv
.venv\Scripts\activate
uv pip install openai python-dotenv fastapi uvicorn pydantic
uv pip freeze > requirements.txt
```

### 验证环境

```powershell
python --version
python -c "import openai, fastapi, pydantic; print('env ok')"
```

预期输出：

```text
Python 3.11.14
env ok
```

## 环境变量配置

本项目使用 `.env` 管理 API Key、模型名称和 Base URL。

```env
OPENAI_API_KEY=your_api_key
BASE_URL=https://api.deepseek.com

DEFAULT_MODEL=deepseek-v4-flash
FLASH_MODEL=deepseek-v4-flash
PRO_MODEL=deepseek-v4-pro
```

说明：

- `OPENAI_API_KEY`：模型平台 API Key，目前使用 OpenAI SDK 兼容接口
- `BASE_URL`：模型服务 Base URL，使用 DeepSeek 时配置为 `https://api.deepseek.com`
- `DEFAULT_MODEL`：默认模型
- `FLASH_MODEL`：适合简单任务、快速任务、低成本任务
- `PRO_MODEL`：适合复杂分析、长文本理解、复杂推理任务

注意：`.env` 已加入 `.gitignore`，不要将真实 API Key 提交到 GitHub。

## 核心模块

### Prompt Library

Prompt 模板库位于：

```text
prompts/
├── research/
│   └── industry-summary.md
├── dev/
│   └── code-explanation.md
└── agent/
    └── task-decomposition.md
```

当前已完成 9 个 Prompt 模板：

- Research Prompt 1：基础行业信息总结
- Research Prompt 2：带分类判断的行业信息总结
- Research Prompt 3：Few-shot 行业信息总结
- Dev Prompt 1：基础代码解释
- Dev Prompt 2：结构化代码分析
- Dev Prompt 3：Few-shot 代码解释
- Agent Prompt 1：基础任务拆解
- Agent Prompt 2：带优先级与依赖关系的任务拆解
- Agent Prompt 3：Few-shot 任务拆解

### ModelClient

模型调用封装位于：

```text
packages/model_client.py
```

当前支持：

- `.env` 配置读取
- DeepSeek API 调用
- `default` / `flash` / `pro` 三类模型选择
- 普通文本调用
- 流式文本调用

示例调用：

```python
from packages.model_client import ModelClient

client = ModelClient()

result = client.chat(
    user_message="用三句话解释什么是 Prompt Engineering。",
    model_type="flash",
)

print(result)
```

### Structured Output

结构化输出模型位于：

```text
packages/structured_output.py
```

当前实现：

- `SummaryResult`：行业信息总结结果
- `ClassifyResult`：行业信息分类结果
- `ExtractResult`：行业信息抽取结果
- `parse_summary()` / `parse_classify()` / `parse_extract()`
- `safe_parse_summary()` / `safe_parse_classify()` / `safe_parse_extract()`

该模块用于将 LLM 输出的 JSON 数据转换为可校验、可复用的 Pydantic 对象。

## 运行方式

### ModelClient 测试

```powershell
python packages\model_client.py
```

该命令会测试：

- Default Model Test
- Flash Model Test
- Pro Model Test
- Streaming Flash Model Test

### Prompt API 测试

```powershell
python -m tests.prompt_api_tests
```

该命令会测试：

- Dev Prompt 3 个
- Agent Prompt 3 个

测试结果输出到：

```text
docs/notes/prompt-api-test-results.md
```

### Structured Output API 测试

```powershell
python -m tests.structured_output_api_test
```

该命令会测试：

- summary API 输出
- classify API 输出
- extract API 输出
- Pydantic 校验结果

测试结果输出到：

```text
docs/notes/structured-output-api-test-results.md
```

## Git 使用记录

当前项目已完成：

- 本地 Git 仓库初始化
- 第一次项目结构提交
- 远程 GitHub 仓库绑定
- 首次推送到 GitHub
- D1 - D4 阶段代码与文档持续提交

第一次提交记录：

```text
7ccd0b0 init nexus ai lab project structure
```

## 当前进度

- [x] D1：项目定位与环境搭建
- [x] D2：Prompt 基础
- [x] D3：结构化输出
- [x] D4：LLM API 调用封装
- [ ] D5：Function Calling
- [ ] D6：FastAPI AI 服务
- [ ] D7：复盘与包装

## W1 交付清单

- [x] GitHub 仓库：包含清晰 README 和基础运行方式
- [x] Prompt 模板库：至少 9 个 Prompt，覆盖总结、抽取、分类、任务拆解、代码解释
- [x] Prompt 测试记录：完成 Research 手动测试、Dev / Agent API 测试
- [x] 模型调用封装：ModelClient 支持普通调用、流式输出、flash / pro 模型选择
- [x] 结构化输出模型：实现 summary / classify / extract 三类 Pydantic 模型与 API 测试
- [ ] FastAPI Demo：提供 `/chat`、`/summarize`、`/plan` 三个接口
- [x] 开发日志：记录每天学到的内容、遇到的问题和解决方案
- [ ] Demo 素材：至少 3 张截图或 1 分钟录屏，为后续简历和面试准备素材

## 已完成能力

### D1：项目定位与环境搭建

完成内容：

- 明确 AI 应用开发工程师能力模型
- 使用 uv 创建 Python 3.11 虚拟环境
- 初始化 Git / GitHub 仓库
- 建立项目目录结构
- 建立 docs 分层文档体系
- 将计划文档 Markdown 化，便于 GitHub 浏览
- 将实习计划图加入项目文档

### D2：Prompt 基础

完成内容：

- 学习 Prompt Engineering 基础结构
- 理解 Role、Task、Context、Input、Constraints、Output Format、Few-shot
- 编写 Research / Dev / Agent 三类 Prompt 模板
- 完成 9 个 Prompt 模板初版
- 使用 DeepSeek V4 手动测试 Research Prompt 3 个
- 使用 ModelClient API 测试 Dev / Agent Prompt 6 个
- 根据测试结果优化 Research Prompt

### D3：结构化输出

完成内容：

- 理解 JSON、JSON Schema、Pydantic 的关系
- 实现 `SummaryResult`、`ClassifyResult`、`ExtractResult`
- 实现结构化输出解析与安全解析函数
- 完成本地正常数据测试
- 完成本地异常数据测试
- 使用 LLM API 完成 summary / classify / extract 连接测试
- 使用 Pydantic 校验 LLM 结构化输出

### D4：LLM API 调用封装

完成内容：

- 理解 LLM API 调用流程
- 理解 system message、user message、temperature、streaming
- 封装 `ModelClient`
- 支持 default / flash / pro 模型选择
- 支持普通调用与流式调用
- 解决 Responses API 与 DeepSeek 兼容性问题，改为 Chat Completions 兼容版
- 使用 ModelClient 闭环 D2 / D3 遗留 API 测试任务

## 当前技术栈

- Python 3.11
- uv
- OpenAI Python SDK
- DeepSeek API
- python-dotenv
- Pydantic
- FastAPI
- Uvicorn
- Git / GitHub
- Markdown

## 后续计划

D5 将进入 Function Calling / Tool Calling 学习，重点完成：

- 理解“模型负责决策，工具负责执行”的基本思想
- 实现网页摘要占位工具
- 实现任务清单生成工具
- 将工具调用结果整理为可复用示例
- 为 D6 FastAPI AI 服务封装做准备

D6 将进入 FastAPI AI 服务封装，重点完成：

- 封装 `/chat` 接口
- 封装 `/summarize` 接口
- 封装 `/plan` 接口
- 将 ModelClient、Prompt Library、Structured Output 接入 API 服务

D7 将进行 W1 复盘与项目包装，重点完成：

- README 最终整理
- 周总结
- Demo 截图或录屏
- W2 计划准备
- 可展示项目材料整理