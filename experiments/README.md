# 实验目录（强制规范）

## 目录结构

```
experiments/
├── README.md
├── baseline/          # 基线：config.yaml / command.txt / notes.md / metrics.csv
├── exp01_xxx/         # 实验 1（后缀用描述性名称，如 exp01_qos01）
├── exp02_xxx/         # 实验 2
└── exp03_xxx/         # 实验 3
```

## 每个实验至少记录（新建实验时复制以下模板）

```markdown
# Experiment ID
EXP-001

## Purpose
验证……

## Compared with
Baseline

## Configuration
...

## Dataset
...

## Random seed
...

## Command
...

## Result
...

## Conclusion
...

## Problems
...
```

## 规则

- 实验编号从 EXP-001 递增，与 [docs/03-design/experiment_design.md](../docs/03-design/experiment_design.md) 的实验矩阵对应。
- 每次实验至少记录上方全部字段，不得缺项。
- 大体积输出（日志、checkpoint）放 `../results/`（不入库），实验目录只保留脚本、配置与小结。
- 指标计算与评测结果放 `../evaluation/`。
- 新实验目录命名：`exp<编号>_<描述>`，如 `exp02_qos01`。
