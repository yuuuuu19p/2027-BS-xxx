# Baseline 说明

## 定义

本地 LLM 直接问答（**no-RAG**）：用户问题直接送入模型，不注入任何检索上下文。
作为后续 RAG 链路的**对照组**（EXP-001），用于回答"RAG 前后回答质量差多少"。

## 组成（已定）

- 模型：qwen2.5:1.5b-instruct-q4_K_M（INT4 / Q4_K_M，GGUF，1.1 GB）
- 引擎：Ollama 0.40.0（Windows；对比 INT8 用 q8_0，见 EXP-004）
- 输入：标准问题集 50 题（`data/samples/standard_questions.jsonl`）
- 输出：逐题回答 + 性能指标（时延、token/s）+ 资源指标（显存/内存）
  - 原始日志：`results/logs/baseline_run1.jsonl`
  - 汇总指标：`metrics.csv` + 问题分析：`baseline_analysis.md`

## 评测方式

- 质量：RAGAS（faithfulness、answer_relevancy；context_relevancy 记为 N/A，因无检索）+ 人工抽检（待装 ragas 后补跑）
- 资源：nvidia-smi（显存峰值 3.35 GB）、ollama 进程内存（57 MB 常驻）
- 性能：avg 3.07 s/题、37.4 tok/s、ttft 211 ms（热态，RTX 4060）

## 与后续实验的关系

- EXP-005：RAG 前后对比（Baseline vs exp01_rag_link）
- EXP-003/EXP-004：模型大小、量化方案对比（INT4 vs INT8、0.5B/1.5B/3B 等）

## 注意事项（实际运行补充）

- 冷启动：首次请求约 55 s（模型加载入显存），后续热态正常；正式部署需预加载/常驻。
- 网络：本机无法直接访问 registry.ollama.ai（`ollama pull` 卡在 manifest），改用 ModelScope 下载 GGUF + `ollama create` 导入，命令见 `command.txt`。
- 中文编码：调用 Ollama API 必须按 UTF-8 发送 JSON（PowerShell 5.1 需显式 UTF-8 字节，Python urllib 默认正确）。
- 系统提示词：加入"校园问答助手、仅依据资料回答"类 system prompt 后，小模型回答质量明显改善；仍属 no-RAG 基线，不引入检索变量。
