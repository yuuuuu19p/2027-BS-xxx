# Baseline 说明

## 定义

本地 LLM 直接问答（**no-RAG**）：用户问题直接送入模型，不注入任何检索上下文。
作为后续 RAG 链路的**对照组**（EXP-001），用于回答"RAG 前后回答质量差多少"。

## 组成

- 模型：qwen2.5:1.5b-instruct-q4_K_M（待定，对比 INT8 用 q8_0）
- 引擎：Ollama（待定，可换 llama.cpp）
- 输入：标准问题集 N 题（待定 50–100）
- 输出：逐题回答 + 性能指标（时延、token/s）+ 资源指标（显存/内存）

## 评测方式

- 质量：RAGAS（faithfulness、answer_relevancy；context_relevancy 记为 N/A，因无检索）+ 人工抽检
- 资源：nvidia-smi（显存）、系统监视（内存）
- 结果记录：metrics.csv + results/logs/ 下的 jsonl 日志

## 与后续实验的关系

- EXP-005：RAG 前后对比（Baseline vs exp01_rag_link）
- EXP-003/EXP-004：模型大小、量化方案对比

## 注意事项

（跑完后补充：模型加载耗时、首次请求冷启动、Ollama 常驻内存等）
