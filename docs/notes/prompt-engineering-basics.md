# Prompt Engineering 基础

## 1. Prompt 是什么

Prompt 是用户给大语言模型的输入指令，用于触发模型生成回答。Prompt 可以是问题、任务说明、上下文、示例、格式要求，也可以包含角色设定和约束条件。

## 2. Prompt Engineering 是什么

Prompt Engineering 是设计和优化输入提示词的过程，目标是让模型更稳定、更准确、更符合预期地完成任务。

## 3. 高质量 Prompt 的组成

一个高质量 Prompt 通常包含：

- Role：角色设定
- Task：任务说明
- Context：上下文背景
- Input：输入内容
- Constraints：约束条件
- Output Format：输出格式
- Examples：示例
- Edge Cases：边界情况

## 4. D2 重点能力

今天重点练习：

- 角色设定
- 任务边界
- 输入输出约束
- Few-shot 示例
- Prompt 模板化

## 5. Prompt 编写原则

- 指令要清晰具体
- 背景信息要充分
- 输出格式要明确
- 复杂任务要拆解
- 不要让模型猜测缺失信息
- 对关键任务提供示例
- 根据输出结果迭代优化

## 6. 通用模板

```text
你是一个 {role}。

你的任务是：{task}

背景信息：
{context}

输入内容：
{input}

约束条件：
1. {constraint_1}
2. {constraint_2}
3. {constraint_3}

输出格式：
{output_format}