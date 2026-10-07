# 问题跟踪

> 状态：打开 / 进行中 / 已解决 / 已关闭（不可复现）

| # | 日期 | 问题描述 | 影响范围 | 状态 | 解决方案 / 关闭说明 |
|---|---|---|---|---|---|
| 1 | 2026-10-07 | 本机无法访问 registry.ollama.ai，`ollama pull` 卡在 manifest 阶段 | 模型获取 | 已解决 | 改从 ModelScope 下载 GGUF + `ollama create` 导入（见 `experiments/baseline/command.txt`） |
| 2 | 2026-10-07 | Baseline 回答幻觉严重：如"校园报警电话"答"110"、图书馆时间编造 | 回答质量 | 进行中 | 对策=引入 RAG 注入校园知识库；详见 `experiments/baseline/baseline_analysis.md` |
| 3 | 2026-10-07 | PowerShell 5.1 调 Ollama API 中文乱码（非 UTF-8） | 评测脚本调试 | 已解决 | 显式 UTF-8 字节发送；Python 脚本默认正确 |
