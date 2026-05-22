# Day 02 开发日志：Prompt 基础

## 今日目标

- 学习 Prompt Engineering 基础结构
- 理解 Role、Task、Context、Input、Constraints、Output Format、Edge Cases、Examples、Few-shot
- 编写 Research / Dev / Agent 三类 Prompt 模板
- 完成 9 个 Prompt 模板初版
- 对 Prompt 进行基础测试

## 今日完成

- [x] 创建 Prompt 文档目录
- [x] 创建 Prompt Engineering 学习笔记
- [x] 编写行业信息总结 Prompt 3 个
- [x] 编写代码解释 Prompt 3 个
- [x] 编写任务拆解 Prompt 3 个
- [x] 使用 DeepSeek V4 手动测试 Research Prompt 3 个
- [x] 记录 Research Prompt 测试结果
- [x] 根据测试结果优化 Research Prompt
- [ ] Dev Prompt 3 个 API 测试
- [ ] Agent Prompt 3 个 API 测试

## 测试策略说明

D2 已完成 Research 类 Prompt 的手动测试。Dev 与 Agent 类 Prompt 将在 D4 完成 ModelClient 封装后，通过 API 方式进行统一测试。

这样做的原因是：

- Dev 与 Agent Prompt 更适合通过标准化输入批量测试
- API 测试可以保留完整输入、输出、模型参数和响应结构
- 后续可复用同一套测试流程评估不同模型效果

## Prompt 优化总结

Research Prompt 测试结果整体符合预期。根据测试表现，完成了以下轻量优化：

- 对 JSON 输出类 Prompt 增加“只输出原始 JSON 对象”的约束
- 限制 `key_points` 数量，提升后续结构化存储和前端展示稳定性
- 对 Few-shot Prompt 增加“避免绝对化表达”的约束，提升行业研究表达严谨性

Dev 与 Agent 类 Prompt 将在 D4 完成 ModelClient 后，通过 API 方式统一测试。

## 今日理解

Prompt Engineering 的核心不是写一句“帮我做什么”，而是通过角色、任务、上下文、约束条件、输出格式和示例，让模型稳定地产出符合预期的结果。

Few-shot 的作用是通过少量示例让模型学习目标输出风格，适合用于风格统一、分类判断、结构化总结和复杂任务拆解。

## 遗留任务

- [ ] D4 使用 API 测试 Dev Prompt 3 个
- [ ] D4 使用 API 测试 Agent Prompt 3 个
- [ ] 将测试结果整理为可复用的 Prompt 评估表

## 明日计划

D3 将学习结构化输出，重点理解 JSON Schema、Pydantic、稳定结构化输出和异常输出修复。