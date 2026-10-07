# 2027-BS-xxx

> 本科毕业设计（2027 届）—— 课题名称占位

## 项目简介

（待填写：课题背景、研究目标、核心贡献）

## 目录结构

```
2027-BS-xxx/
├── docs/          # 文档：选题、文献、设计、会议纪要
├── src/           # 核心源代码
├── configs/       # 配置文件
├── scripts/       # 辅助脚本（数据处理、训练、可视化等）
├── data/          # 数据（仅存小样本，大文件不入库）
├── experiments/   # 实验（baseline / exp01 / exp02 ...）
├── results/       # 实验结果（表格、图、日志、checkpoint）
├── thesis/        # 论文（大纲、图表、草稿、参考文献）
└── progress/      # 进度管理（里程碑、周志、问题跟踪）
```

各目录用途详见对应目录下的 README / 模板文件。

## 快速开始

（待填写：环境依赖、安装与运行方式）

## 进度

- 里程碑：[progress/milestones.md](progress/milestones.md)
- 周志：[progress/weekly_log.md](progress/weekly_log.md)
- 问题跟踪：[progress/issues.md](progress/issues.md)

## 仓库约定

- 大文件（原始数据、checkpoint、日志等）不入库，见 `.gitignore` 与 [data/README.md](data/README.md)。
- 文档以 Markdown 维护，公式/图直接引用 `docs/03-design/figures`、`thesis/figures`。
- 会议纪要按 `docs/04-meetings/YYYY-MM-DD.md` 命名。
